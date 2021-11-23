import redis5
r = redis5.Redis(db=1,host='85.208.253.188')

#r.set("hello","reza")
#print(r.get("hello"))
#print(r.delete("hello"))
#r.set('name', 'reza') # True
#r.db.delete("hello",True)
#r.incr("countr")
r.decr("countr")
#r.delete("hello")
r.flush()
# value = r.get('hello')
# print(value) # 'world'
# r.delete('hello') # True
# print(r.get('hello')) # None