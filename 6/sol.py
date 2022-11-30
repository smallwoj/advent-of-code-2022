import sys
text = sys.stdin.read()

input = list(text)

yea = []
while input:
    yea.append(input.pop(0))
    if len(set(yea[-4:])) == 4:
        break

print(f'part 1: {len(yea)}')
input = list(text)

yea = []
while input:
    yea.append(input.pop(0))
    if len(set(yea[-14:])) == 14:
        break

print(f'part 2: {len(yea)}')
