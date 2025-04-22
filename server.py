# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow requests from Unity

latest_heartbeat = 0

@app.route('/api/heartbeat', methods=['POST'])
def receive_heartbeat():
    global latest_heartbeat
    data = request.get_json()
    if 'heartbeat' in data:
        latest_heartbeat = data['heartbeat']
        print(f"Received heartbeat: {latest_heartbeat}")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "No heartbeat provided"}), 400

@app.route('/api/heartbeat', methods=['GET'])
def get_heartbeat():
    return jsonify({"heartbeat": latest_heartbeat})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
