# import sys
#
# sys.stdin = open("in1.txt", 'rt')

n = int(input())
meetings = list(list(map(int, input().split())) for _ in range(n))
meetings.sort(key=lambda x: x[1])

cnt = 1
last_order = meetings[0][1]
# print(f"meeting starts {meetings[0][0]} to {meetings[0][1]}")
for meeting in meetings:
    start = meeting[0]
    end = meeting[1]

    if start >= last_order:
        last_order = end
        cnt += 1
        # print(f"meeting starts {start} to {end}")

# print('\n'.join(' '.join(map(str, sl)) for sl in meetings))
# print(f"cnt : {cnt}")
print(cnt)
