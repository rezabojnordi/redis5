import redis

class Redis:
    def __init__(self,db=0,host="127.0.0.1",port=6379,password=''):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.r = redis.Redis(
        host = self.host,
        port = self.port,
        db = self.db,
        password = self.password)
        self.data = {self.db: {}}
    def get(self, key):
        """Gets the value associated with a key"""
        data = self.r.get(key)
        obj = {"key":key, "value":data,"db":self.db}
        return obj
    def set(self, key, value):
        """Sets a key-to-value association"""
        self.r.set(key,value)
        return True
    def delete(self, key):
        """Deletes a key"""
        del self.data[self.db][key]
        return True  





# r = redis.Redis(
#     host='85.208.253.188',
#     port=6379,
#     password='')


# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)


# r = redis.Redis(host='localhost', port=6379, db=1)

# r.set('hello', 'world') # True

# value = r.get('hello')
# print(value) # b'world'

# r.delete('hello') # True
# print(r.get('hello')) # None