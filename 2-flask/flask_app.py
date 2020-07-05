from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def default_route():
    return "Hello!"


@app.route("/client/info")
def client_info_route():
    user_agent = request.headers.get("USER_AGENT")
    return {"user_agent": user_agent}


if __name__ == "__main__":
    app.run(port=8000, debug=True)
