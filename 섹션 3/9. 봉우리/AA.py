# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())
arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
arr.insert(0, [0] * (n + 2))
arr.append([0] * (n + 2))

res = 0


def is_this_peak(a, i, j):
    middle_num = a[i][j]
    if a[i - 1][j] < middle_num and a[i][j - 1] < middle_num and a[i][j + 1] < middle_num and a[i + 1][j] < middle_num:
        return True
    else:
        return False


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if is_this_peak(arr, i, j):
            res += 1

print(res)
