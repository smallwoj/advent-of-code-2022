import sys
input = [x.strip() for x in sys.stdin.readlines()]

def priority(c: str) -> int:
    if ord(c) in range(ord('a'), ord('z')+1):
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 1 + priority('z')

s = 0

for rucksack in input:
    compartments = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    
    overlap = set(compartments[0]).intersection(set(compartments[1]))
    s += priority(overlap.pop())

print(f'part 1: {s}')
s=0
for i in range(0, len(input), 3):
    
    
    overlap = set(input[i]).intersection(set(input[i+1])).intersection(set(input[i+2]))
    s += priority(overlap.pop())

print(f'part 2: {s}')
