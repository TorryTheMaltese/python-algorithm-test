import sys

# sys.stdin = open("in1.txt", "r")


def state_dfs(v):
    if v == n + 1:
        for i in range(1, len(arr)):
            if arr[i] > 0:
                print(i, end=" ")
        print()
        return
    else:
        arr[v] = 1
        state_dfs(v + 1)
        arr[v] = 0
        state_dfs(v + 1)


if __name__ == "__main__":
    n = int(input())
    arr = [0] * (n + 1)
    state_dfs(1)
