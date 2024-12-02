import urllib.request
import re

l1 = []
l2 = []

with open("input.txt", "r") as data:
    for d in data:
        pair = re.split(r'\s+', d.strip())
        l1.append(pair[0])
        l2.append(pair[1])

answer = 0

for l in l1:
    appearance = l2.count(l)
    answer += int(l) * appearance

print(answer)