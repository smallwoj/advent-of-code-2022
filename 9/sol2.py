import sys, math
input = [s.strip() for s in sys.stdin.readlines()]

worm = [[0,0] for _ in range(10)]

def touching(p1, p2) -> bool:
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])

    local_min = min(dx, dy)
    local_max = max(dx, dy)

    diagonal_steps = local_min
    straight_steps = local_max - local_min
    result = diagonal_steps + straight_steps

    return result == 1 or result == 0

def all_touching():
    t = True
    for i in range(1, len(worm)):
        if not touching(worm[i-1], worm[i]):
            t = False
    return t

tail_visited = set()

for motion in input:
    dir, steps = motion.split()
    steps = int(steps)
    for i in range(steps):
        prev = [[*seg] for seg in worm]
        if dir == 'U':
            worm[0][1] += 1
        elif dir == 'D':
            worm[0][1] -= 1
        elif dir == 'R':
            worm[0][0] += 1
        elif dir == 'L':
            worm[0][0] -= 1
        while not all_touching():
            for i in range(1, len(worm)):
                if not touching(worm[i-1], worm[i]):
                    dx = worm[i-1][0] - worm[i][0]
                    dy = worm[i-1][1] - worm[i][1]
                    dx = dx // abs(dx) if dx else 0
                    dy = dy // abs(dy) if dy else 0
                    worm[i] = [worm[i][0] + dx, worm[i][1] + dy]
        tail_visited.add(tuple(worm[-1]))

print(f'part 2: {len(tail_visited)}')
