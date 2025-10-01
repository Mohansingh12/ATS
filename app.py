from flask import Flask, jsonify, request, render_template
import os,requests

LLM_ENDPOINT = os.getenv('LLM_ENDPOINT', 'http://localhost:12434/v1/completions')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    payload = {
        "model": "gemma3",
        "prompt": 'hi how are you',
        "max_tokens": 100,
        "temperature": 0.7
    }
    response = requests.post(LLM_ENDPOINT, json=payload, timeout=30)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
