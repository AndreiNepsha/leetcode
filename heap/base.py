def parent(node):
    return node // 2


def right(node):
    return node * 2 + 1


def left(node):
    return node * 2


class MaxPrioirutyQueue:
    def __init__(self, cap) -> None:
        self.n = 0
        self.pq = [None] * (cap + 1)

    def get_max(self):
        return self.pq[1]

    def insert(self, element):
        self.n += 1
        self.pq[self.n] = element
        self._swim(self.n)

    def delete_max(self):
        _max = self.pq[1]
        self._exchange(self.n, 1)
        self.pq[self.n] = None
        self.n -= 1
        self._sink(1)
        return _max

    def _swim(self, k):
        while k > 1 and self._less(parent(k), k):
            self._exchange(parent(k), k)
            k = parent(k)

    def _sink(self, k):
        while left(k) <= self.n:
            older = left(k)
            if right(k) <= self.n and self._less(older, right(k)):
                older = right(k)
            if self._less(older, k):
                break
            self._exchange(older, k)
            k = older

    def _exchange(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def _less(self, i, j):
        return self.pq[i] < self.pq[j]

