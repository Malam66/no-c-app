from flask import Flask, render_template, request, jsonify, send_file
import subprocess
import threading
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_app', methods=['POST'])
def start_app():
    try:
        # Start ONLY the new app
        subprocess.Popen([sys.executable, 'ultimate_gaming_app.py'])
        return jsonify({"status": "success", "message": "NEW APP started successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download')
def download_app():
    try:
        # Send ONLY the new app file
        return send_file('ultimate_gaming_app.py', 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app.py',
                        mimetype='text/plain')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download_package')
def download_package():
    try:
        # Create a zip package with ONLY new app
        import zipfile
        zip_filename = 'ultimate_gaming_app_new.zip'
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Add ONLY new app
            zipf.write('ultimate_gaming_app.py', 'ultimate_gaming_app.py')
            # Add requirements
            zipf.write('requirements.txt', 'requirements.txt')
            # Add README
            zipf.write('README_NEW.md', 'README.md')
            # Add installer
            zipf.write('install_new.bat', 'install.bat')
        
        return send_file(zip_filename, 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app_new.zip',
                        mimetype='application/zip')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
