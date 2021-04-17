# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())

players = list(list(map(int, input().split())) for _ in range(n))

cnt = 0

for player in players:
    height = player[0]
    weight = player[1]
    flag = True

    for i in range(n):
        if players[i][0] > height and players[i][1] > weight:
            flag = False

    if flag:
        # print(player)
        cnt += 1

print(cnt)
