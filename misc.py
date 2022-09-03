UPLOAD_FOLDER = './temp_files'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
    '''
    Breaks down the file name and checks that extension matches
    ALLOWED_EXTENSIONS
    '''
    name, ext = filename.split('.', 2)
    if(ext in ALLOWED_EXTENSIONS):
        return True
    return False