from flask import Flask, jsonify, request
import os,requests

OLLAMA = os.getenv("OLLAMA_ENDPOINT", "http://ollama:11434")
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask + Ollama!"
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)
    prompt = data.get("prompt","Hello from Flask + Ollama!")
    payload = {"model":"gemma3", "prompt": prompt, "stream": False}
    r = requests.post(f"{OLLAMA}/api/generate", json=payload, timeout=120)
    r.raise_for_status()
    return jsonify(r.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
