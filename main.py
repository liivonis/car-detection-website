from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import os
import mysql.connector
import db_connection

db = db_connection.mycursor

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'videos'
app.secret_key = 'the random string'


ALLOWED_EXTENSIONS = set(['mp4'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def upload_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash('File successfully uploaded')
            db.execute("INSERT INTO videos (VideoName) VALUES ('%s')" % filename.split('.')[0])
            db_connection.mydb.commit()
            return redirect('/')
        else:
            flash('Incorrect file format')
            return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
