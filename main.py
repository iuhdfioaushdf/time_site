from flask import Flask
import time
import os

app = Flask(__name__)

@app.route("/time/")
def index():

    time_obj = str(time.time())

    return time_obj


if __name__ == '__main__':

    with app.app_context():
        port = int(os.environ.get("PORT", 8800))
        app.run(host='0.0.0.0', port=port, debug=True)