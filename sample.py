from redis import Redis

conn = Redis(host="localhost")

conn.flushall()