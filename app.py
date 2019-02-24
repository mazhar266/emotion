import os
import uuid
import datetime

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from config import SETTINGS
from utils import is_allowed_file, get_cassandra_session

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = SETTINGS["UPLOAD_FOLDER"]
app.config['MAX_CONTENT_LENGTH'] = SETTINGS["MAX_CONTENT_LENGTH"]

session = get_cassandra_session()


# the root url containing app info
@app.route('/')
def info():
    return jsonify(SETTINGS["INFO"])


# the file upload url
@app.route('/api/v1/image', methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            return jsonify({"success": False})

        file = request.files['image']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({"success": False})
        if file and is_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            uuid_val = uuid.uuid1()
            filename = "{}#{}".format(uuid_val, filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # now insert into cassandra
            # filename
            session.execute(
                """
                INSERT INTO images (id, path, uploaded)
                VALUES (%s, %s, %s)
                """,
                (uuid_val, filename, datetime.datetime.now())
            )

            return jsonify({
                "success": True,
                "id": uuid_val
            })

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=image>
            <input type=submit value=Upload>
        </form>
        '''


# read the file
@app.route('/api/v1/image/<image_id>', methods=["GET"])
def read_file(image_id):
    try:
        rows = session.execute('SELECT * FROM images where id={}'.format(image_id))
        if rows[0]:
            return send_from_directory(SETTINGS["UPLOAD_FOLDER"], rows[0].path)

        return jsonify({
            "success": False
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })
