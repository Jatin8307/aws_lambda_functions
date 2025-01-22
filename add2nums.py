import json

def lambda_handler(event, context):
    try:
        # Retrieve numbers from event body
        body = json.loads(event['body'])
        num1 = body.get('num1')
        num2 = body.get('num2')
        
      # numbers are valid or not
        if num1 is None or num2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Please provide both num1 and num2')
            }
        
        
        result = num1 + num2
        
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

