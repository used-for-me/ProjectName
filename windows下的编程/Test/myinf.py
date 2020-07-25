class MyInf:
    def __init__(self):
        self.number = 0#
        self.rere = 0
        self.yu = 0
        self.sign = True

    def __add__(self, other):
        if type(other) == MyInf:
            self.number += other.number
