import threading


class Milk(object):
    sum_lock = threading.Lock()

    def __init__(self, my_sum):
        self.sum = my_sum
        self.status = True

    @classmethod
    def create(cls, *args, **kwargs):
        if not hasattr(Milk, 'locked'):
            with Milk.sum_lock:
                if not hasattr(Milk, 'locked'):
                    Milk.locked = Milk(*args, **kwargs)
        return Milk.locked

    def seller(self):
        self.sum -= 1
        if self.sum + 1 <= 0:
            self.status = False
        return self.status, self.sum

    def add(self, add_sum):
        self.sum += add_sum


def seller_milk():
    for k in range(15):
        buyer = Milk.create(100)
        print(buyer.seller())


# seller_milk()
for i in range(10):
    thread = threading.Thread(target=seller_milk)
    thread.start()

6