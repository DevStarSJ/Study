def handler(packages, event):
    requests = packages['requests']
    
    request_url = event['queryStringParameters']['url']
    response = requests.get('http://' + request_url)

    return { 'body': { 'url': request_url, 'text': response.text } }