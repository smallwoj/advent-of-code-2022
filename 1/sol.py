import sys
input = sys.stdin.read()
elves = input.split('\n\n')
parsed_elves = []
for elf in elves:
    parsed_elf = [int(cal) for cal in elf.split('\n')]
    parsed_elves.append(parsed_elf)

result = max(parsed_elves, key=sum)
print(f'part 1: {sum(result)}')

s = 0
for _ in range(3):
    result = max(parsed_elves, key=sum)
    parsed_elves.remove(result)
    s += sum(result)
print(f'part 2: {s}')
