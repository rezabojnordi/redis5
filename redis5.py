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
        self.db.delete(key)
        return True  
    
    def incr(self, key):
        if (self.r.get(key) == None):
            self.r.set(key,1)
            print("create" + key)
        else:
            self.r.incr(key)
        return  self.r.get(key)
    
    def decr(self, key):
        if (self.r.get(key) == None or int(self.r.get(key)) <= 0):
            print("check")
            return self.r.get(key)
        else:
            print("incrept")
            self.r.decr(key)
        return  self.r.get(key)







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