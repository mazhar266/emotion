## Emotion

This is a REST API enabled image micro-service. This service can upload and store images, also serve the original and resized thumb images. It stores data in a Cassandra data store.

### Requirements

- Python 3.6 or later
- Cassandra 3 or later
- ImageMagick 7 or later
- Python Flask

### How to run

- Install Cassandra and keep running
- Install Python 3 and pip 3
- Install dependencies like `python3 -m pip install -r requirements`
- Run `python3 setup_db.py` to setup the db for the first time
- Or execute the `db.sql` in database manually
- Run `flask run`
- or run `FLASK_DEBUG=1 flask run` (this will reload on changes)
- or run `./run.sh`

### How to upload file

Just send the file as **POST** in `/api/v1/image` and you will be returned with an ID. For making it easier to understand, it will genarate a form if a **GET** request is sent in `/api/v1/image`.

### How to use the file

Send a **GET** request at

- `/api/v1/image/<ID>` will return the original file
- `/api/v1/image/<ID>?width=<X>&height=<Y>` will return the resized file

### TODO

- Implement security check
- Implement Token based auth
- Implement Aspect Ratio check
- Implement Crop
- Implement Rotation
- Implement Watermark
- Implement Masking
- Make sure generated UUID is unique
- Write tests
- Implement Docker
- Implement AWS Lambda, S3 support

### Contribution Guideline

- Fork and submit a pull request
- Maintain PEP8 convension
- Check your code using pylint

### Credits

- Mazhar Ahmed - [github.com/mazhar266](https://github.com/mazhar266)
