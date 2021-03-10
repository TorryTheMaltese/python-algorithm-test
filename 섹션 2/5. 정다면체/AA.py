# import sys
#
# sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())
d = dict()
cnt = 0
res = list()

for i in range(2, n + m + 1):
    d[i] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i + j] += 1

for key, val in d.items():
    if val > cnt:
        cnt = val
        res.clear()
        res.append(key)
    elif val == cnt:
        res.append(key)

# print(d)
# print(res)

print(*res, sep=" ")
