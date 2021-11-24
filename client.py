import redis5
r = redis5.Redis(db=1,host='85.208.253.188')

#r.set("hello","reza")
#print(r.get("hello"))
#print(r.delete("hello"))
#r.set('name', 'reza') # True
#r.db.delete("hello",True)
r.incr("countr")
#r.decr("countr")
#r.delete("hello")
#r.flush()
# value = r.get('hello')
# print(value) # 'world'
# r.delete('hello') # True
# print(r.get('hello')) # None
#print(r.list_keys())
#print(r.add_key('reza','reza'))
#print(r.rpush('RR',"[1,2,3,5,5]"))
#print(r.lpush('RR','BR'))
#print(r.lpop('RR'))
#print(r.rpop('RR'))
##print(r.llen('RR'))
# print(r.lindex('RR',3))
#print(r.lrange('RR',2))
#print(r.rpush('RR',2))
#print(r.expire('RR',20))
#print(r.ttl('RR'))
print(r.type('R'))