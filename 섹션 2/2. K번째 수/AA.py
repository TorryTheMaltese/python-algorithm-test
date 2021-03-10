# import sys
# sys.stdin = open("in2.txt", "r")

cases = input()

for case in range(int(cases)):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = arr[s - 1:e]
    tmp.sort()
    print(f'#{case + 1} {tmp[k-1]}')
