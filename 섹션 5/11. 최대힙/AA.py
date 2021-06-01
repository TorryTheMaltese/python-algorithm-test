import sys
import heapq

# sys.stdin = open("in1.txt", "rt")

heap = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n, n))
