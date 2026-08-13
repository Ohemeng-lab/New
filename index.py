from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

@app.route('/api/hello')
def hello():
    return jsonify({"hello": "world"})

@app.route('/api/status')
def status():
    return jsonify({"status": "ok"})
