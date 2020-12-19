import redis
import base64
import md5
import sys
import hashlib

class UrlShortener:
    def __init__(self):
        self.redis = redis.StrictRedis(host=localhost,
                                       port=6379,
                                       db=db0)
        
    def idToShortURL(id): 
        Map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        shortURL = "" 
        while(id > 0): 
            shortURL += Map[id % 62] 
            id //= 62
        return shortURL[len(shortURL): : -1] 

    def shortURLToId(shortURL): 
        id = 0
        for i in shortURL: 
            val_i = ord(i) 
            if(val_i >= ord('a') and val_i <= ord('z')): 
                id = id*62 + val_i - ord('a') 
            elif(val_i >= ord('A') and val_i <= ord('Z')): 
                id = id*62 + val_i - ord('Z') + 26
            else: 
                id = id*62 + val_i - ord('0') + 52
        return id
    
    def getshortURL(id):
        shortURL = idToShortURL(id) 
        print("Short URL from 12345 is : ", shortURL) 
        print("ID from", shortURL, "is : ", shortURLToId(shortURL))
       
    def sha512encode(url):    
        message = hashlib.sha512()
        message.update(url)
        return base64.urlsafe_b64encode(
            message.hexdigest().encode("utf-8"))[:6].decode("utf-8")    
        
    def shortcode(self, url):
        return base64.b64encode(md5.new(url).digest()[-4:]).replace('=','').replace('/','_')

    def shorten(self, url):
        code = self.shortcode(url)
        try:
            self.redis.set(config.REDIS_PREFIX + code, url)
            return {'success': True,
                    'url': url,
                    'code': code,
                    'shorturl': config.URL_PREFIX + code}
        except:
            return {'success': False}

    def lookup(self, code):
        try:
            return self.redis.get(config.REDIS_PREFIX + code)
        except:
            return None
