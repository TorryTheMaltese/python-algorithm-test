import sys
import heapq

# sys.stdin = open("in1.txt", "rt")

heap = []

while True:
    n = int(input())
    if n > 0:
        heapq.heappush(heap, n)
    elif n == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print("-1")
    elif n == -1:
        break
