import sys
input = sys.stdin.readline

n = int(input())

all = list()

for _ in range(n):
    data = int(input())
    all.append(data)

count = 0
start = 0

for i in range(1, n+1):
    target = all[-i]
    if target > start:
        count += 1
        start = target

print(count)