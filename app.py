from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        #should probably check to make sure the file is a csv
        #then perform a check to look for address/Address column
        file = request.files['file']
        file.save(secure_filename("upload_"+file.filename))
        print(type(file))
    
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)