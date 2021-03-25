# import sys
#
# sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lt = 0
rt = n - 1

while True:
    mid = (lt + rt) // 2
    if arr[mid] == m:
        print(mid + 1)
        break
    elif arr[mid] > m:
        rt = mid - 1
    elif arr[mid] < m:
        lt = mid + 1