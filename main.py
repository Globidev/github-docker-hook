import sys

hook = __import__(sys.argv[1])

from flask import Flask, request

app = Flask(__name__)

import logging

app.logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s -- %(levelname)s]\t%(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

import threading
import traceback

def call_hook(payload):
    try:
        hook.on_push(payload, app.logger)
    except Exception:
        app.logger.error('Error while executing hook')
        app.logger.error(traceback.format_exc())

@app.route(hook.ROUTE, methods=['POST'])
def on_push():
    payload = request.get_json()
    hook_thread = threading.Thread(
        target=call_hook,
        args=(payload,)
    )
    hook_thread.start()

    return 'Ok!'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=hook.PORT,
    )
