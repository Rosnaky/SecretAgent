import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/index.html")
def site_index():
    return flask.render_template("index.html")

@app.route("/app.html")
def site_app():
    return flask.render_template("app.html")

if __name__ == "__main__":
    app.run(port=3000)