import sys

# sys.stdin = open("in3.txt", "r")


def dfs(v, sum):
    global n, coins, m, cnt, res
    if sum==m:
        if v<res:
            res = v
        return
    if v>res:
        return
    else:
        for coin in coins:
            if sum+coin<=m:
                dfs(v+1, sum+coin)


if __name__ == "__main__":
   n = int(input())
   coins = list(map(int, input().split()))
   m = int(input())

   coins.sort(reverse=True)
   cnt = 0
   res = 999999

   dfs(0,0)
   print(res)
