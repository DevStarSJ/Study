def handler(event):
    user_id = event['queryStringParameters']['id']
    return { 'body': { 'id': user_id, 'name': "test" } }