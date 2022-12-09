import sys
input = [s.strip() for s in sys.stdin.readlines()]

head = [0, 0]
tail = [0, 0]

def tail_touching() -> bool:
    return tail[0] + 1 == head[0] or tail[0] - 1 == head[0] or tail[1] + 1 == head[1] or tail[1] - 1 == head[1]

tail_visited = set()
tail_visited.add(tuple(tail))

count = 1
for motion in input:
    dir, steps = motion.split()
    steps = int(steps)
    for i in range(steps):
        if dir == 'U':
            head[1] += 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail[1] += 1
        elif dir == 'D':
            head[1] -= 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail[1] -= 1
        elif dir == 'R':
            head[0] += 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail[0] += 1
        elif dir == 'L':
            head[0] -= 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail[0] -= 1
        tail_visited.add(tuple(tail))

for x in range(min([x[0] for x in tail_visited]), max([x[0] for x in tail_visited])):
    for y in range(min([x[1] for x in tail_visited]), max([x[0] for x in tail_visited])):
        if x == 0 and y == 0:
            c = 's'
        elif (x, y) in tail_visited:
            c = '#'
        else:
            c = '.'
        print(c, end='')
    print()
print(f'part 1: {len(tail_visited)}')