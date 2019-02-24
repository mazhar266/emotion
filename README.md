## Emotion

This is the image service of TicketChai

### Requirements

- Python 3.6 or later
- Cassandra 3 or later
- ImageMagick 7 or later

### How to run

- Install Cassandra and run
- Install Python
- Install dependencies like `python3 -m pip install -r requirements`
- Run `python3 setup_db.py` to setup the db for the first time
- Or execute the `db.sql` in database manually
- Run `flask run`
- or run `FLASK_DEBUG=1 flask run` (this will reload on changes)
- or run `./run.sh`

### How to upload file

Just send the file as POST in `/api/v1/image` and you will be returned with an ID

### How to use the file

Send a GET request at

- `/api/v1/image/<ID>` will return the original file
- `/api/v1/image/<ID>?width=<X>&height=<Y>` will return the resized file


### Credits

- Mazhar Ahmed
- Hosne Mubarak Rubai

> Copyright (c) Systech Unimax Limited, TicketChai Limited
