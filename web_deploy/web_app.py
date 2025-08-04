from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_app', methods=['POST'])
def start_app():
    try:
        # Start the app in background
        subprocess.Popen([sys.executable, 'app.py'])
        return jsonify({"status": "success", "message": "App started successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
