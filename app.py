import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import openai

app = Flask(__name__)
# CORS設定を更新
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-app-node-12.azurewebsites.net",
            "http://localhost:3000" # ローカル開発⽤
        ]
    }
})

@app.route('/')
def home():
    return "Welcome to the Flask API! Use /api/process for POST requests."

# Set your OpenAI API key
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

@app.route('/api/process', methods=['POST'])
def process_data():
    # Get JSON data from the request
    data = request.get_json()

    # Extract the event, emotion, and opinion from the input
    event = data.get('event')
    emotion = data.get('emotion')
    opinion = data.get('opinion')

    if not all([event, emotion, opinion]):
        return jsonify({"error": "All fields (event, emotion, opinion) are required."}), 400

    client = OpenAI(api_key=api_key)

    try:

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは回答者に寄り添い、肯定的かつ励ます伴走者です。"},
                {"role": "user", "content": (
                    "３つの回答内容から読み取れる価値観やその説明を200文字程度で複数挙げてください。"
                    "あなたは回答者に対して肯定的で励ますような寄り添う伴走者です。"
                    "伴走者としての回答者へのメッセージも含めて作成してください。\n"
                    f"回答1: {event}\n"
                    f"回答2: {emotion}\n"
                    f"回答3: {opinion}"
                )}
            ]
        )

# JSON 形式で出力
        
        # Extract the response text
        value_analysis = completion.choices[0].message.content.strip()


        return jsonify({"value_analysis": value_analysis})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
     # 環境変数PORT を取得（デフォルトは8000）
     port = int(os.environ.get('PORT', 8080))
     # デバッグモードをローカル環境では有効に、本番では無効に
     app.run(host='0.0.0.0', port=port, debug=False)
