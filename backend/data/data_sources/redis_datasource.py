from redis import Redis
from redis.cache import CacheConfig
import json
class RedisDatasource(object):
    conn = None
    def __new__(cls):
      
        if not hasattr(cls,'cache_instance'):
            cls.cache_instance = super(RedisDatasource,cls).__new__(cls)
        if cls.conn == None:
            cls.cache_instance.conn = Redis(host="localhost",port=6379,decode_responses=True)
        return cls.cache_instance
    
    def setCacheData(self,key,value):
        self.conn.setex(key,300,value)

    def setJsonData(self,key,json_data):
        data = json.dumps(json_data)
        self.conn.setex(key,300,data)
        return data

    def getCacheData(self,key):
        return self.conn.get(key)
    
    def getJsonCacheData(self,key):
        cached_data = self.conn.get(key)
        if(cached_data != None):
            return json.loads(self.conn.get(key))

        
        return None 