# import redis
# import threading
#
#
# my_redis = redis.Redis(password='myredismimo')
# local = threading.local()
# local.redis = {}
# print(local.redis)

import threading

import redis

# 这是一个特殊的对象
local = threading.local()  # 先实例化一个对象
local.redis = {}


def key_for(user_id):
    return "account:{}".format(user_id)


def _lock(client, key):
    print(key)
    return bool(client.set(key, value="True", nx=True, ex=5))


def _unlock(client, key):
    client.delete(key)


def lock(client, user_id):
    key = key_for(user_id)
    if key in local.redis:
        local.redis[key] += 1
        return True
    ok = _lock(client, key)
    print(ok)
    if not ok:
        return False
    local.redis[key] = 1
    return True


def unlock(client, user_id):
    key = key_for(user_id)
    if key in local.redis:
        local.redis[key] -= 1
        if local.redis[key] <= 0:
            del local.redis[key]
            _unlock(client, key)
        return True
    return False


client1 = redis.Redis(password='myredismimo')
print("lock:", lock(client1, "codehole"))
print("lock:", lock(client1, "codehole"))
print("unlock:", unlock(client1, "codehole"))
print("unlock:", unlock(client1, "codehole"))
