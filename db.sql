-- create keyspace
CREATE KEYSPACE emotion
  WITH REPLICATION = {
   'class' : 'SimpleStrategy',
   'replication_factor' : 1
  };

-- create table
CREATE TABLE emotion.images (
	id UUID PRIMARY KEY,
	path text,
	uploaded timestamp,
);