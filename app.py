from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


latest_data = {}  # เก็บข้อมูลล่าสุด

@app.route('/api/data', methods=['POST'])
def receive_data():
    global latest_data
    latest_data = request.json
    return jsonify({'message': 'Data received'}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(debug=True)
