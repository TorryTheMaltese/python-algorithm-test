import sys
sys.stdin = open("in1.txt", "rt")

cards = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in range(10):
    a, b = map(int, input().split())
    cards.sort(key=lambda rng:cards[a:b])

print(cards)