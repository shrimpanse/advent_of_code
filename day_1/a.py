import urllib.request
import re

l1 = []
l2 = []

with open("input.txt", "r") as data:
    for d in data:
        pair = re.split(r'\s+', d.strip())
        l1.append(pair[0])
        l2.append(pair[1])

l1 = sorted(l1)
l2 = sorted(l2)

answer = 0
for i in range(len(l1)):
    answer += abs(int(l1[i]) - int(l2[i]))

print(answer)