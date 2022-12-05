import sys, re
input = [x.strip() for x in sys.stdin.readlines()]

count = 0
for pair in input:
    min1, max1, min2, max2 = map(int, re.split(r',|-', pair))
    if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
        count += 1

print(f'part 1: {count}')
count=0
for pair in input:
    min1, max1, min2, max2 = map(int, re.split(r',|-', pair))
    if set(range(min1, max1+1)).intersection(set(range(min2, max2+1))):
        count+=1
print(f'part 2: {count}')
