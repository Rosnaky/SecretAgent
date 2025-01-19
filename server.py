import subprocess
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/")
@app.route("/index.html")
def site_index():
    return flask.render_template("index.html")


@app.route("/app.html")
def site_app():
    return flask.render_template("app.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = flask.request.json


    input_text = data.get("input", "")

    print(f"Received input: {input_text}")

    process = subprocess.run(
        ["python", "driver.py", input_text],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    return flask.jsonify({"message": "Input received!", "input": input_text})


if __name__ == "__main__":
    app.run(port=3001)
