# import sys
#
# sys.stdin = open("in3.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

left = 1
right = 2

a.insert(0, 0)

total = a[left]

while left < n:
    if right <= n:
        total = total + a[right]

        if total == m:
            cnt += 1

        if total >= m:
            left += 1
            right = left + 1
            total = a[left]
        else:
            right += 1
    else:
        break
        # left += 1
        # right = left + 1
        # total = a[left]

a.pop(0)

print(cnt)
