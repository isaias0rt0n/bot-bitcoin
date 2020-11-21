import ssl
import json

import websocket
from pyexpat.errors import messages


def on_open(ws):
    print("opened the connection")

    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""

    ws.send(json_subscribe)


def on_close(ws):
    print("### closed ###")


def on_message(ws, message):
    message = json.loads(message)
    print(message['data']['price'])


def on_error(ws, error):
    print("gave error")
    print(error)





if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=on_open,
                                on_close=on_close,
                                on_message=on_message,
                                on_error=on_error)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})