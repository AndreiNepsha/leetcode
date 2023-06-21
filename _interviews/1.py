
g = dict()

n = int(input())
for i in range(n):
    try:
        s = input().split(" ")
        g[s[0]] = s[2:]
    except:
        pass

printed = set()
def print_names(f):
    try:
        if f not in printed:
            for d in g[f]:
                print_names(d)
            printed.add(f)
            print(f, end=" ")
    finally:
        pass

for f in g.keys():
    print_names(f)
