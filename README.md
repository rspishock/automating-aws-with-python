# automating-aws-with-python

Repository for automating AWS with Python.  Scripts are a project files from an A Cloud Guru series on utilizing Python to work with AWS.

## 01-webotron

webotron is a script that will sync a local directory to an s3 bucket, and optionally configure Route 53 and cloudfront as well.

### Features

webotron current has the following features:

- List bucket
- List contents of a bucket
- Create and set up bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>
- Configure Route 53 domain

## 02-notifon

Notifon is a project to notify Slack users of changes to your AWS account using CloudWatch Events.

### Features

Notifon currently has the following features:

- Send notifications to Slack when CloudWatch Events happen.
