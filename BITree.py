
class BITIndexError(IndexError): pass

class BITree:
    def __init__(self, sz):
        self.size = sz
        self.arr = [0] * (sz + 1)
        self.sums = [0] * (sz + 1)

    def add(self, i, dx):
        self._checkInd(i)
        arr, sums = self.arr, self.sums
        arr[i] += dx

        while i <= self.size:
            sums[i] += dx
            i += i&-i

    def update(self, i, x):
        self._checkInd(i)
        self.add(i, x - self.arr[i])

    def sum(self, i=None):
        if i is None: i = self.size
        self._checkInd(i)

        sums = self.sums
        s = 0
        while i > 0:
            s += sums[i]
            i -= i&-i

        return s

    def sumRange(self, i0, i1):
        if i0 > i1: raise Exception(f'i0 > i1')
        if i0 <= 1: return self.sum(i1)
        return self.sum(i1) - self.sum(i0-1)

    def _checkInd(self, i):
        if i <= 0 or i > self.size:
            raise BITIndexError(f'index out of range: {i} (sz={self.size})')
