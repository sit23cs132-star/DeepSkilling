import json

def lambda_handler(event, context):
    """
    AWS Lambda function handler for HTTP API or Event bridge execution.
    """
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from AWS Lambda for Week 7!',
            'input_event': event
        })
    }
