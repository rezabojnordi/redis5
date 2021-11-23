import redis5
r = redis5.Redis(db=1,host='85.208.253.188')

r.set("hello","reza")
print(r.get("hello"))
# r.set('hello', 'world') # True
# value = r.get('hello')
# print(value) # 'world'
# r.delete('hello') # True
# print(r.get('hello')) # None