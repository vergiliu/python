from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def index():
    return 'this is the index'

@app.route("/error/keepalive.jsp")
def reply_w_error():
    abort(408)

@app.route("/<app_name>/keepalive.jsp")
def keepalive_reply(app_name):
    print('checking {}'.format(app_name))
    return 'OK'

if __name__ == '__main__':
    app.run(port=8888)
