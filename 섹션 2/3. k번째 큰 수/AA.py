# import sys
# sys.stdin = open("in2.txt", "rt")

n, k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

res = set()
for first in range(n-2):
    for seconds in range(first + 1, n-1):
        for last in range(seconds + 1, n):
            res.add(cards[first] + cards[seconds] + cards[last])
result = list(res)
result.sort(reverse=True)
print(result[k-1])

