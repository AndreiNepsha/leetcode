from collections import Counter


def parent(node):
    return node // 2


def right(node):
    return node * 2 + 1


def left(node):
    return node * 2


class PrioirutyQueue:
    def __init__(self, cap, cmp=None) -> None:
        """cmp - False element at the top"""
        self.n = 0
        self.pq = [None] * (cap + 1)
        self.cmp = cmp
        if not self.cmp:
            self.cmp = lambda z, y: z < y

    def get_head(self):
        return self.pq[1]

    def insert(self, element):
        self.n += 1
        self.pq[self.n] = element
        self._swim(self.n)

    def pop_head(self):
        if self.n == 0:
            return None
        _max = self.pq[1]
        self._exchange(self.n, 1)
        self.pq[self.n] = None
        self.n -= 1
        self._sink(1)
        return _max

    def _swim(self, k):
        while k > 1 and self._cmp(parent(k), k):
            self._exchange(parent(k), k)
            k = parent(k)

    def _sink(self, k):
        while left(k) <= self.n:
            older = left(k)
            if right(k) <= self.n and self._cmp(older, right(k)):
                older = right(k)
            if self._cmp(older, k):
                break
            self._exchange(older, k)
            k = older

    def _exchange(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def _cmp(self, i, j):
        return self.cmp(self.pq[i], self.pq[j])


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter()
        for t in tasks:
            counter.update(t)
        pq = PrioirutyQueue(len(counter), lambda x, y: x[1] > y[1])
        for c in counter.values():
            pq.insert((c - 1, 0))
        tact = 0
        while True:
            t = pq.get_head()
            if t is None:
                return tact
            if t[1] <= tact:
                pq.pop_head()
                if t[0] > 0:
                    pq.insert((t[0] - 1, t[1] + n + 1))
            tact += 1


class SimpleSolution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        l = [counter[i] for i in counter]
        m = max(l)
        m_count = 0
        for e in l:
            if m == e:
                m_count += 1
        return max(len(tasks), (m - 1) * (n + 1) + m_count)


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
a = SimpleSolution().leastInterval(tasks, n)
assert 8 == a, a

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
a = SimpleSolution().leastInterval(tasks, n)
assert 16 == a, a
