import requests
import websockets
import asyncio
import json

@asyncio.coroutine
def echo():
    ws_url = None
    bot_id = None
    res =requests.post('https://slack.com/api/rtm.start',
        data={'token' : 'xoxb-98124228960-QR2JPnavuZLX60ejqW1rwRQZ'}).json()

    if res.get('ok'):
        ws_url = res.get('url') # wss url
        print(ws_url)
        bot_id = res.get('self').get('id')
        print(bot_id)
    else:
        print('RTM Start Failed...')

    ws = yield from websockets.connect(ws_url)

    while True:
        recv_msg = yield from ws.recv()
        recv_json = json.loads(recv_msg)
        print(recv_json)
        if recv_json.get('type') == 'message' and recv_json.get('text').startswith('<@{}>'.format(bot_id)):
            msg = recv_json.get('text').split(' ',1)
            print('msg : ', msg)
            yield from ws.send(json.dumps({"id": 1, "type" : "message", "channel": recv_json.get('channel'),
                "text": '<@{0}> {1}'.format(recv_json.get('user'), msg[1])}))

asyncio.get_event_loop().run_until_complete(echo())
