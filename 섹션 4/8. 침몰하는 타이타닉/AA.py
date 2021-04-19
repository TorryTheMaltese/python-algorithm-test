# import sys
#
# sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())

weights = list(map(int, input().split()))
cnt = 0

while len(weights) > 0:
    weights.sort(reverse=True)
    if len(weights) > 1:
        total = weights[0] + weights[-1]
        if total > m:
            weights.pop(0)
            cnt += 1
        else:
            weights.pop(0)
            weights.pop(-1)
            cnt += 1
    else:
        weights.pop()
        cnt += 1

print(cnt)
