import redis
import json
from config import redis_url, redis_port

class Cache:
    r = redis.Redis(host=redis_url, port=redis_port, decode_responses=True)

    try:
        REDIS_SERVER_REPONSE = r.ping()

        print(f"Pinged Redis. You successfully connected to Redis")

    except Exception as e:
        print(e)
    

    