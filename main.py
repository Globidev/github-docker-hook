import sys

hook = __import__(sys.argv[1])

from flask import Flask, request

app = Flask(__name__)

@app.route(hook.ROUTE, methods=['POST'])
def on_push():
    payload = request.get_json()
    hook.on_push(payload)
    return 'Ok!'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=hook.PORT,
        debug=True
    )
