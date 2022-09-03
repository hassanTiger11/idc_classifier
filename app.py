
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from misc import allowed_file, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    '''
    This request for debugging
    '''
    return "<p>Hello, World!</p>"

@app.route('/upload_pic', methods=['POST'])
def upload_pic():
    # check if the post request has the file part
    print("function called uplaod_pic, path = /upload_pic")
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "saved"


@app.route('/analyze', methods=['POST'])
def analyze_pic():
    val = ''

    return val