import boto3
import click
import mimetypes
from botocore.exceptions import ClientError
from pathlib import Path

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')


@click.group()
def cli():
    """webotron deploys websites to AWS"""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets"""
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an s3 bucket"""
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure s3 bucket"""
    s3_bucket = None

    try:
        s3_bucket = s3.create_bucket(
            Bucket=bucket
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            # prints error that bucket is already owned by user
            s3_bucket = s3.Bucket(bucket)
        else:
            # raises error
            raise e

    policy = """
    {
        "Version": "2012-10-17",
        "Statement":[{
        "Sid":"PublicReadGetObject",
        "Effect":"Allow",
        "Principal":"*",
            "Action":["s3:GetObject"],
            "Resource":["arn:aws:s3:::%s/*"
            ]
            }
        ]
    }
    """ % s3_bucket.name
    policy = policy.strip()  # strips new line from front of JSON file

    pol = s3_bucket.Policy()
    pol.put(Policy=policy)  # adds policy to bucket

    ws = s3_bucket.Website()
    ws.put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }
    })

    return


def upload_file(s3_bucket, path, key):
    content_type = mimetypes.guess_type(key)[0] or 'text/plain'  # checks file type, default to plain
    s3_bucket.upload_file(
        path,
        key,
        ExtraArgs={
            'ContentType': 'text/html'
        })


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET"""
    s3_bucket = s3.Bucket(bucket)
    root = Path(pathname).expanduser().resolve()
    
    def handle_directory(target):
        for p in target.iterdir():
            if p.is_dir():
                handle_directory(p)
            if p.is_file():
                upload_file(s3_bucket, str(p), str(p.relative_to(root)))
            
    handle_directory(root)


if __name__ == '__main__':
    cli()
