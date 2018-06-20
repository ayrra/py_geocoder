from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import csv_helpers as csv_h
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    global file_name
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("temp_"+file.filename))
        file_name = file.filename

        if csv_h.contains_address("temp_"+file_name):
            csv_h.return_new_csv("temp_"+file_name)
            os.remove("temp_"+file_name)
            return render_template("index.html",btn="download.html",geo_html="geo_"+file_name[:-4]+".html")
        else:
            os.remove("temp_"+file_name)
            return render_template("index.html",error_msg="File does not contain Address or address column!")

@app.route('/download')
def download():
    return send_file("geo_"+file_name, attachment_filename="geo_"+file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)