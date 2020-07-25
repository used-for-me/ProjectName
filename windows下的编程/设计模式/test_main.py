import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, hh):
        time.sleep(1)
        self.hh = hh

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                # print(Singleton._instance_lock)
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

    def prints(self):
        self.hh -= 1
        print(self.hh)


def task(arg):
    obj = Singleton.instance(100)
    obj.prints()


for i in range(100):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

time.sleep(20)
obj = Singleton.instance()
# print(obj)
