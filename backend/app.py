from flask import Flask, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return Response("Hello from Effective Mobile!", mimetype="text/plain")


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200