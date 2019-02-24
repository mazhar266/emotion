from cassandra.cluster import Cluster

from config import SETTINGS

cluster = Cluster(SETTINGS["CASSANDRA"]["HOST"])
session = cluster.connect()

# create the database
session.execute("CREATE KEYSPACE emotion WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")
# create the table
session.execute("CREATE TABLE emotion.images (id UUID PRIMARY KEY, path text, uploaded timestamp)")
print("Database initiated successfully")
