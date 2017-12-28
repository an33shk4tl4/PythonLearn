import redis

redis_server = '192.168.56.103'
conn = redis.Redis(redis_server, 6379)
print(conn.ping())
print(conn.keys('user:name'), conn.get('user:name'))
