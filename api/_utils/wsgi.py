from flask import Flask
from api._utils.flask import send_file, bundle_lib
import os

app = Flask(__name__)
@app.route('/')
def home():
    return bundle_lib("src/routes/index.html")

@app.route('/assets/<path:file_path>')
def serve_app_files(file_path):
    return send_file("public/" + file_path)

@app.route('/lib/<path:file_path>')
def serve_lib_files(file_path):
    full_path = os.path.join("src/lib/" + file_path)
    return send_file(full_path)
    
@app.route("/<path:file_path>")
def use_template(file_path):
    full_path = os.path.join("src/routes/" + file_path + "/index.html" )
    return bundle_lib(full_path)

if __name__ == "__main__":
    app.run(debug=True)