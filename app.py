from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask API! Use /api/process for POST requests."

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json
    feel = data.get('feel')
    event = data.get('event')
    emotion = data.get('emotion')
    opinion = data.get('opinion')

    # 仮のvaluesデータ
    values = {
        "value_analysis": "あなたの価値観は新しいことに挑戦することです。",
        "recommendation": "挑戦を続けることでさらなる成長が期待されます。",
    }

    return jsonify(values=values)

if __name__ == '__main__':
    app.run(port=5000)
