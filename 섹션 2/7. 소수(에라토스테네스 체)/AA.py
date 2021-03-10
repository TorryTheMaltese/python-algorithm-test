# # import sys
# #
# # sys.stdin = open("in1.txt", "rt")
#
#
# def prime_list(x):
#     sieve = [True] * (x + 1)
#
#     # sqrt(x) == x^(0.5) : x의 최대 약수가 sqrt(x) 이하이므로 sqrt(x)까지 검사
#     # m = int(x ** 0.5)
#     # for i in range(2, m+1):
#
#     for i in range(2, x + 1):
#         if sieve[i]:
#             for j in range(i + i, x + 1, i):
#                 sieve[j] = False
#
#     cnt = 0
#     for i in range(2, x + 1):
#         if sieve[i]:
#             cnt += 1
#     print(cnt)
#
#
# n = int(input())
# prime_list(n)

# import sys
# sys.stdin=open("input.txt", "r")
n = int(input())
ch = [0] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1
print(cnt)
