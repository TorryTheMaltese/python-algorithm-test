import sys

# sys.stdin = open("in1.txt", "r")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # DFS를 이용한 수들의 조합 # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# def dfs(v, s):
#     global cnt
#     if v==k:
#         if sum(res)%m==0:
#             cnt+=1
#
#     else:
#         for i in range(s, n):
#             res[v] = nums[i]
#             dfs(v+1, i+1)
#
#
# if __name__ == "__main__":
#     n, k = map(int, input().split())
#     nums = list(map(int, input().split()))
#     m = int(input())
#
#     res = [0]*k
#     cnt = 0
#     dfs(0,0)
#     print(cnt)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # 라이브러리를 이용한 수들의 조합 # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import itertools


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())

    cnt = 0

    for tmp in itertools.combinations(nums, k):
        if sum(tmp)%m==0:
            cnt+=1
    print(cnt)
