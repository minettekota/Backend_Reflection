from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# CORS設定を更新
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-app-py-12.azurewebsites.net",
            "http://localhost:3000" # ローカル開発⽤
        ]
    }
})

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
     # 環境変数PORT を取得（デフォルトは8000）
     port = int(os.environ.get('PORT', 8000))
     # デバッグモードをローカル環境では有効に、本番では無効に
     app.run(host='0.0.0.0', port=port, debug=False)
