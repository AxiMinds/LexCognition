# app.py

from flask import Flask, request, jsonify
from lexnlp.nlp_processor import NLPProcessor

app = Flask(__name__)
nlp_processor = NLPProcessor()

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text')
    task = data.get('task')
    api = data.get('api', 'ollama')
    model = data.get('model')

    if not text or not task:
        return jsonify({"error": "Missing text or task"}), 400

    try:
        result = nlp_processor.process_text(text, task, api, model)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)# app.py

from flask import Flask, request, jsonify, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from lexnlp.nlp_processor import NLPProcessor

app = Flask(__name__)
auth = HTTPBasicAuth()
nlp_processor = NLPProcessor()

users = {
    "admin": generate_password_hash("password123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
@auth.login_required
def process_text():
    data = request.json
    text = data.get('text')
    task = data.get('task')
    api = data.get('api', 'ollama')
    model = data.get('model')

    if not text or not task:
        return jsonify({"error": "Missing text or task"}), 400

    try:
        if task == 'classification':
            categories = data.get('categories', [])
            result = nlp_processor.text_classification(text, categories)
        elif task == 'ner':
            result = nlp_processor.named_entity_recognition(text)
        elif task == 'sentiment':
            result = nlp_processor.sentiment_analysis(text)
        else:
            result = nlp_processor.process_text(text, task, api, model)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)# app.py

from flask import Flask, request, jsonify, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from lexnlp.nlp_processor import NLPProcessor

app = Flask(__name__)
auth = HTTPBasicAuth()
nlp_processor = NLPProcessor()

users = {
    "admin": generate_password_hash("password123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
@auth.login_required
def process_text():
    data = request.json
    text = data.get('text')
    task = data.get('task')
    api = data.get('api', 'ollama')
    model = data.get('model')

    if not text or not task:
        return jsonify({"error": "Missing text or task"}), 400

    try:
        if task == 'classification':
            categories = data.get('categories', [])
            result = nlp_processor.text_classification(text, categories)
        elif task == 'ner':
            result = nlp_processor.named_entity_recognition(text)
        elif task == 'sentiment':
            result = nlp_processor.sentiment_analysis(text)
        else:
            result = nlp_processor.process_text(text, task, api, model)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)