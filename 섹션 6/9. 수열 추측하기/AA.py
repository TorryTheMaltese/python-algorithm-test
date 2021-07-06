import sys

# sys.stdin = open("in1.txt", "rt")


def calc_triangle(arr):
    b = [1]*n
    total = 0

    for i in range(1, n):
        b[i] = (b[i-1]*(n-i))//i

    for j in range(n):
        total += arr[j]*b[j]
    return total

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # #   DFS를 이용한 수열 추측하기  # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# def dfs(v):
#     global n, f,ch
#     if v==n:
#         if calc_triangle(res)==f:
#             for r in res:
#                 print(r, end=' ')
#             exit()
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0:
#                 res[v] = i
#                 ch[i]=1
#                 dfs(v+1)
#                 ch[i]=0
#         return
#
#
#
#
# if __name__ == "__main__":
#     n, f = map(int, input().split())
#     res = [0]*n
#     ch = [0]*(n+1)
#     dfs(0)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # 라이브러리를 이용한 수열 추측하기 # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import itertools

if __name__ == "__main__":
    n, f = map(int, input().split())
    a = list(range(1, n + 1))
    cnt = 0

    for tmp in itertools.permutations(a, n):
        arr = []
        for t in tmp:
            arr.append(t)
        if calc_triangle(arr)==f:
            for a in arr:
                print(a, end=' ')
            break

