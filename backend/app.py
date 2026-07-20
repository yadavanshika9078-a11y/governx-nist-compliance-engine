from flask import Flask
from flask_cors import CORS

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)


@app.route("/")
def home():
    return {
        "message": "Welcome to GovernX",
        "version": Config.VERSION,
        "status": "Backend is running successfully"
    }


if __name__ == "__main__":
    app.run(debug=Config.DEBUG)