import boto3

profile = input("Profile name: ")
session = boto3.Session(profile_name=profile)  # replace with variable for username
s3 = session.resource('s3')