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
        self.r.delete(key)
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
    
    def flush(self):
        return self.r.flushdb()
    
    def list_keys(self):
        return self.r.smembers('count')
    
    def add_key(self, keyname,values):
        return self.r.sadd(keyname, values)
    
    def rpush(self,key,value):
        return self.r.rpush(key,value)
    
    def rpush(self,key,value):
        return self.r.rpush(key,value)
    

    def lpush(self,key,value):
        return self.r.lpush(key,value)
    

    def rpush(self,key,value):
        return self.r.rpush(key,value)
    

    def lpop(self,key):
        return self.r.lpop(key)
    

    def rpop(self,key):
        return self.r.rpop(key)
    

    def llen(self,key):
        return self.r.llen(key)
    
    def sadd(self,key,value):
        return self.r.llen(key,value)
    


    def lindex(self,key,id):
        return self.r.lindex(key, id)
    

    def lrange(self,key,index0=0,index1=-1):
        return self.r.lrange(key,index0,index1)
    

    def expire(self,key,ttl):
        return self.r.expire(key,ttl)
    

    def ttl(self,key):
        return self.r.ttl(key)
    
        
    def type(self,key):
        return self.r.type(key)
    
    def sort(self,list,start=0,num=-1):
        try:
            return self.r.sort(list,start,num)
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)          # __str__ allows args to be printed directly,
            return False
    
         
    def hset(self,hash,field,value):
        return self.r.hset(hash,field,value)
    
    def hget(self,hash,field):
        return self.r.hget(hash,field)
    
        
    def hgetall(self,hash):
        return self.r.hgetall(hash)
    
    def hexists(self,hash,field):
        return self.r.hexists(hash,field)
    
    def hdel(self,hash,field):
        return self.r.hdel(hash,field)
    
    def hvals(self,hash):
        return self.r.hvals(hash)
    
    def hmget(self,hash,key):
        return self.r.hmget(hash,key)
    
    def rpoplpush(self,list1,list2):
        return self.r.rpoplpush(list1,list2)

        #RPOPLPUSH










