# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())

a = list()

max_total = 0

for i in range(0, n):
    a.append(list(map(int, input().split())))

# 가로 합
for i in range(0, n):
    total = sum(a[i])
    if max_total < total:
        max_total = total

# 세로 합
for i in range(0, n):
    b = [j[i] for j in a]
    total = sum(b)
    if max_total < total:
        max_total = total

# 대각선 합
b = []
for i in range(0, n):
    b.append(a[i][i])
total = sum(b)
if max_total < total:
    max_total = total

b = []
for i in range(0, n):
    b.append(a[i][-(i+1)])
total = sum(b)
if max_total < total:
    max_total = total

print(max_total)
