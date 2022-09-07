
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from misc import allowed_file, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from nn import load_model, predict
import os
app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['model'] = load_model()

@app.route("/")
def hello_world():
    '''
    This request for debugging
    '''
    return "<p>Invasive Ductal Carcinoma Classifier. Please send POST request with you image to '/predict'.</p>"



@app.route('/predict', methods=['POST'])
def analyze_pic():
    '''
    This function will use the same architecture of upload_pic to receive the picture
    Then loads the machine learning model
    Then apply it to the picture
    The return the result
    '''
    # check if the post request has the file part
    print("function called analyze_pic, path = /analyze_pic")

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
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        #predict
        result = predict(app.config['model'], filepath)
        os.remove(filepath)

        if(result == 0):
            return 'healthy tissue'
        return 'possibly idc'
        
    
