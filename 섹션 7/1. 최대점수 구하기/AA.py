import sys


# sys.stdin = open("in1.txt", "r")


def dfs(v, grade, time):
    global res_grade
    if time > m:
        return
    if v == n:
        if grade > res_grade:
            res_grade = grade
        return
    else:
        dfs(v + 1, grade + quest[v][0], time + quest[v][1])
        dfs(v + 1, grade, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    quest = []
    ch = [0] * n

    res_time = 0
    res_grade = 0

    for _ in range(n):
        q = list(map(int, input().split()))
        quest.append(q)
    dfs(0, 0, 0)
    print(res_grade)
