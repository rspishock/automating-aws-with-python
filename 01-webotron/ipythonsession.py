# coding: utf-8

# NOTES:

import boto3

# sets a session variable with given profile name
session = boto3.Session(profile_name='pythonAutomation')

# initializes session
s3 = session.resource('s3')

# displays a list of all s3 buckets
for bucket in s3.buckets.all():
    print(bucket)

# creates a new s3 bucket from boto3
new_bucket = s3.create_bucket(Bucket='pythoncreatedtestbucket')

for bucket in s3.buckets.all():
    print(bucket)

# sets client for ec2
ec2_client = session.client('ec2')