import sys

# sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())
music = list(map(int, input().split()))
all_music = sum(music)
max_value = max(music)

lt = 1
rt = sum(music)
res = 0


def count(max_sum):
    dvd_cnt = 1
    sum_tmp = 0
    for x in music:
        if sum_tmp + x > max_sum:
            dvd_cnt += 1
            sum_tmp = x
        else:
            sum_tmp += x
    return dvd_cnt


while lt <= rt:
    avg = (lt + rt) // 2
    if max_value <= avg and count(avg) <= m:
        res = avg
        rt = avg - 1
    else:
        lt = avg + 1

print(res)
