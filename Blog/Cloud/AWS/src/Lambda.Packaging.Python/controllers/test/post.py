def handler(packages, event):
    user_id = event['queryStringParameters']['id']
    body = event['body']
    header = event['headers']
    return { 'body': { 'id': user_id, 'header': header, 'body': body } }