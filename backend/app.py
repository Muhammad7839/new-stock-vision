from flask import Flask, jsonify
from flask_cors import CORS  # 👈 Add this

app = Flask(__name__)
CORS(app)  # 👈 Allow requests from frontend (important)

@app.route("/api/message")
def message():
    return jsonify({"text": "Hello from your Flask backend!"})

if __name__ == "__main__":
    app.run(debug=True)