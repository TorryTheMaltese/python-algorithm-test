import sys

# sys.stdin = open("in1.txt", "rt")

n, c = map(int, input().split())
stable = list(int(input()) for _ in range(n))
stable.sort()

lt = stable[0]
rt = stable[-1]
res = 0


def count_stable(min_len):
    stable_num = 1
    ep = stable[0]
    for i in range(1, n):
        if stable[i] - ep >= min_len:
            stable_num += 1
            ep = stable[i]
    return stable_num


while lt <= rt:
    mid = (lt + rt) // 2
    if count_stable(mid)>=c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1


print(res)
