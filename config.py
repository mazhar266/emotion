import os

SETTINGS = {
    "INFO": {
        "name": "Emotion",
        "info": "The image micro-service",
        "version": "1.0.0",
    },

    "CASSANDRA": {
        "HOST": ["localhost", ],
        "KEYSPACE": "emotion",
    },
    "BASE_URL": "http://localhost:5000",

    "UPLOAD_FOLDER": os.path.basename('uploads'),
    "CACHE_FOLDER": os.path.basename('cache'),
    "ALLOWED_EXTENSIONS": ['png', 'jpg', 'jpeg', 'gif'],
    "MAX_CONTENT_LENGTH": 16 * 1024 * 1024,
}
