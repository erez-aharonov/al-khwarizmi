import alkh
alkh.analyze()
import pandas as pd


jj = 20
m = 200


class A:
    k = 8
    m = pd.Series({"c": 20})
    m.c = 50

    def __init__(self):
        self.k, ll = 9, 10 + jj
        b, mm = 8 + self.k + self.m.c, self.k
        pass

    @staticmethod
    def run(
            n)\
            -> int:
        a = 5
        b = a + 7 + 5.0
        ll = a + 6.4
        c = a + b + 3
        d = b + c
        k = int(d * 2)
        return k


class B:
    def __init__(self):
        b = 8
        pass

    def run(self):
        a = 5
        b = a + 7 + 5.0
        ll = a + 6.4
        c = a + b + 3
        d = b + c


a = A()
