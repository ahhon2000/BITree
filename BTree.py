
class BTree:
    def __init__(self, sz):
        self.size = sz
        self.arr = [0] * (sz + 1)
        self.sums = [0] * (sz + 1)

    def add(self, i, dx):
        if i <= 0 or i > self.size: raise Exception(f'index out of range: {i}')
        arr, sums = self.arr, self.sums
        arr[i] += dx

        while i <= self.size:
            sums[i] += dx
            i += i&-i

    def update(self, i, x):
        self.add(i, x - self.arr[i])

    def sumAll(self, i=None):
        if i is None: i = self.size
        s = 0
        while i > 0:
            s += sums[i]
            i -= i&-i

        return s

    def sumRange(self, i0, i1):
        if i0 > i1: raise Exception(f'i0 > i1')
        return self.sumAll(i1) - self.sumAll(i0-1)
