import sys
input = [s.strip() for s in sys.stdin.readlines()]
the_map = []

original_start = None
starting = {}
end = None
for i, line in enumerate(input):
    heights = []
    for j, c in enumerate(line):
        if c == 'S':
            starting[(i,j)] = set()
            original_start = (i,j)
            heights.append('a')
        elif c == 'E':
            end = (i, j)
            heights.append('z')
        elif c == 'a':
            starting[(i,j)] = set()
            heights.append(c)
        else:
            heights.append(c)
    the_map.append(heights)

the_map = [[ord(c) for c in line] for line in the_map]

for start in starting:
    visited_points = set()
    visited_paths = set()

    potential_paths = [[start]]

    while potential_paths:
        path = potential_paths.pop(0)
        if path[-1] in visited_points:
            continue
        elif path[-1] == end:
            starting[start].add(tuple(path))
            break
        else:
            x, y = path[-1]
            visited_points.add((x,y))
            curr_elevation = the_map[x][y]
            for i in range(-1,2):
                for j in range(-1,2):
                    if not (abs(i) == abs(j)) :
                        if 0 <= x+i < len(the_map) and 0 <= y+j < len(the_map[0]):
                            if the_map[x+i][y+j] <= curr_elevation + 1:
                                potential_paths.append([*path, (x+i, y+j)])

print(f'part 1: {len(min(starting[original_start], key=len))-1}')
min_lens = [len(min(starting[start], key=len)) for start in starting if starting[start]]
print(f'part 2: {min(min_lens)-1}')
