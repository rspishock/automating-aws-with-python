import os

def post_to_slack(event, context):
    slack_webhook_url = os.environment['SLACK_WEBHOOK_URL']
    print(slack_webhook_url)
    print(event)

    return
