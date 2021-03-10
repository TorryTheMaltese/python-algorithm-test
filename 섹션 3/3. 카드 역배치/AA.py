# import sys
# sys.stdin = open("in1.txt", "rt")

# ------------ my solution ------------
# cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# for n in range(10):
#     a, b = map(int, input().split())
#     cards[a:b+1] = reversed(cards[a:b+1])
#
# print(*cards[1:], sep=" ")
# -------------------------------------


# import sys
#
# sys.stdin = open("input.txt", "r")
# a = list(range(21))
# for _ in range(10):
#     s, e = map(int, input().split())
#     for i in range((e - s + 1) // 2):
#         a[s + i], a[e - i] = a[e - i], a[s + i]
# a.pop(0)
# for x in a:
#     print(x, end=' ')
