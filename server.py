import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

app.run(port=3000)