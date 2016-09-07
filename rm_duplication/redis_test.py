import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'ddddd bar')
s=r.get('foo')
print(s)