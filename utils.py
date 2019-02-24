from cassandra.cluster import Cluster

from config import SETTINGS

cluster = Cluster(SETTINGS["CASSANDRA"]["HOST"])
session = cluster.connect()
session.set_keyspace(SETTINGS["CASSANDRA"]["KEYSPACE"])


def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in SETTINGS["ALLOWED_EXTENSIONS"]


def get_cassandra_session():
    return session
