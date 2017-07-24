import boto3
import json
import sys

import functional as F
import linear as L

BUCKET_NAME = 'dev-tensorflow-savedata'
KEY = 'result.json'
RESULT_FILE = KEY
S3 = boto3.resource('s3')

DEBUG = True
def debug_print(obj):
    if DEBUG:
        print(obj)
    

def get_predict_data():
    try:
        #S3.Bucket(BUCKET_NAME).download_file(KEY, RESULT_FILE)
        with open(RESULT_FILE) as data_file:    
            return json.load(data_file)
    except:
        print(sys.exc_info()[0])
        return None
    return None

def get_x(event):
    get_querystring= F.curryr(F.get)('queryStringParameters')
    get_X = F.curryr(F.get)('X')

    return F.go(event, 
        get_querystring, 
        get_X,
        lambda x: json.loads(x),
        lambda x: [x])

def handler(event, context):
    debug_print(event)

    predict_data = get_predict_data()
    debug_print(predict_data)
    if predict_data is None:
        return {'statusCode': 500}

    X = get_x(event)
    if X is None:
        return {'statusCode': 404}

    W = predict_data['W']
    b = predict_data['b']

    print("L.matmul(X,W)[0] = ",L.matmul(X,W)[0]);

    H = L.matadd(L.matmul(X,W)[0],b)
    S = [L.sigmoid(x) for x in H]
    M = L.softmax(S)
    answer = L.argmax(M)

    debug_print([answer, M])
    debug_print(sum(M))

    body = { 'answer': answer, 'rating': M }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response

if __name__ == "__main__":
    event = {"queryStringParameters": {"X": "[0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0]"}}
    print(handler(event,None))