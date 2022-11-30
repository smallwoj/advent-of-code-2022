import sys, math
input = [s.strip() for s in sys.stdin.readlines()]

head = [0, 0]
tail = [0, 0]

def tail_touching() -> bool:
    dx = abs(tail[0] - head[0])
    dy = abs(tail[1] - head[1])

    local_min = min(dx, dy)
    local_max = max(dx, dy)

    diagonal_steps = local_min
    straight_steps = local_max - local_min
    result = diagonal_steps + straight_steps

    return result == 1 or result == 0

tail_visited = set()
tail_visited.add(tuple(tail))

count = 1
for motion in input:
    dir, steps = motion.split()
    steps = int(steps)
    for i in range(steps):
        prev = [*head]
        if dir == 'U':
            head[1] += 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail = [*prev]
        elif dir == 'D':
            head[1] -= 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail = [*prev]
        elif dir == 'R':
            head[0] += 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail = [*prev]
        elif dir == 'L':
            head[0] -= 1
            if head == tail:
                count += 1
            elif not tail_touching():
                tail = [*prev]
        tail_visited.add(tuple(tail))

print(f'part 1: {len(tail_visited)}')
