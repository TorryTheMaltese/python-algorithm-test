import sys

# sys.stdin = open("in1.txt", "rt")

n = int(input())
pre_written = []
written = []

for _ in range(n):
    pre_written.append(input())

for _ in range(n - 1):
    written.append(input())

for w in written:
    if w in pre_written:
        pre_written.remove(w)

print(pre_written.pop())

