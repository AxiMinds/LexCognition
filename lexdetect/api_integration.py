from flask import Flask, request, jsonify
from .detection_algorithm import detect_human_vs_ai

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_text():
    data = request.json
    text = data.get('text', '')
    result = detect_human_vs_ai(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
