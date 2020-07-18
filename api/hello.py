from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/users")
def users():
    return jsonify(
        [
            {"id": 1, "name": "Bret", "email": "Sincere@april.biz"},
            {"id": 2, "name": "Antonette", "email": "Shanna@melissa.tv"},
        ]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
