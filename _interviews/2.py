from collections import defaultdict, deque

n, k = input().split(" ")
n, k = int(n), int(k)
windows = defaultdict(deque)
for _ in range(k):
    time, token = input().split(" ")
    time = int(time)
    window = windows[token]
    while len(window) and time - window[0] >= 1000:
        window.popleft()
    if not len(window) or len(window) < n and time - window[0] < 1000:
        print(time, token)
        window.append(time)
