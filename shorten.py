import redis
import base64
import md5
import sys

class UrlShortener:
    def __init__(self):
        self.redis = redis.StrictRedis(host=localhost,
                                       port=6379,
                                       db=db0)
        
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
