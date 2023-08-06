from flask import Flask
from config import DevConfig
from waitress import serve

app = Flask(__name__)
app.config.from_object(DevConfig)


# -----ROUTES------------------------------------------------------------------
@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello World! This is some more text.</h1>"
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    # app.run()
    serve(app, host="0.0.0.0", port=5000)
