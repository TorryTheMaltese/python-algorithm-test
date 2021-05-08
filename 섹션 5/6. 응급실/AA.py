import sys

# sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())
patients = list(map(int, input().split()))
cnt = 0

tmp = patients[m]
patients[m] = 0

while True:
    if patients[0] == 0:
        if tmp < max(patients[1:]):
            t = patients.pop(0)
            patients.append(t)
        else:
            cnt += 1
            break
    else:
        if patients[0] < max(patients[1:]) or patients[0] < tmp:
            t = patients.pop(0)
            patients.append(t)
        else:
            patients.pop(0)
            cnt += 1

print(cnt)
