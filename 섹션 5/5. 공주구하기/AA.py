import sys
from collections import deque

# sys.stdin = open("in1.txt", "rt")

n, k = map(int, input().split())
queue = deque()
for i in range(1, n + 1):
    queue.append(i)

while len(queue)>1:
    queue.rotate(-(k-1))
    queue.popleft()

result = queue.pop()
print(result)
