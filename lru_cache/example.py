from time import time

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


@cache
def factorial_with_cache(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


start = time()
print(factorial(100))
print(time() - start)
start = time()
print(factorial_with_cache(200))
print(time() - start)

