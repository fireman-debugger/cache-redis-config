import os
import json
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

class RedisConfig:
    def __init__(self):
        self.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value, expiration=None):
        if expiration:
            self.redis.setex(key, value, expiration)
        else:
            self.redis.set(key, value)

    def delete(self, key):
        self.redis.delete(key)

def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config

config = load_config()
redis_config = RedisConfig()

def main():
    if config['use_redis']:
        redis_config.redis.ping()

if __name__ == '__main__':
    main()