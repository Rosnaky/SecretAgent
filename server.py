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

test_info = {
    "tests": [
        {"id": 0, "name": "Client Code Safety", "status" : "Pending", "raw_data": []},
        {"id": 1, "name": "SQL Injection", "status" : "Pending", "raw_data": []},
        {"id": 2, "name": "Cross Site Scripting (XSS)", "status" : "Pending", "raw_data": []},
        {"id": 3, "name": "Brute Force Attack", "status" : "Pending", "raw_data": []},
        {"id": 4, "name": "Directory Exposure", "status" : "Pending", "raw_data": []},
        {"id": 5, "name": "Network Request Exposure", "status" : "Pending", "raw_data": []},
    ],
    "recommendations" : ""
}

@app.route("/api/tests", methods=["GET"])
def get_tests():
    return flask.jsonify(test_info)

@app.route("/api/tests/<int:test_id>", methods=["PATCH"])
def update_test(test_id):
    test = next((test for test in test_info["tests"] if test["id"] == test_id), None)
    if test:
        updates = flask.request.json
        test.update(updates)
    return flask.jsonify(test)

if __name__ == "__main__":
    app.run(port=3001)
