import os

SETTINGS = {
    "INFO": {
        "name": "TicketChai Emotion",
        "info": "The image service of TicketChai",
        "version": "1.0.0",
    },

    "CASSANDRA": {
        "HOST": ["localhost", ],
        "KEYSPACE": "emotion",
    },

    "UPLOAD_FOLDER": os.path.basename('uploads'),
    "ALLOWED_EXTENSIONS": ['png', 'jpg', 'jpeg', 'gif'],
    "MAX_CONTENT_LENGTH": 16 * 1024 * 1024,
}