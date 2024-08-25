import json
#
def lambda_handler(event, context):
    # TODO implement
    print('another print statement again deleted')
    print('done')
    print('lambda modified on Aug-24')
    print('it's again')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! fellow mate')
    }
