import sys
input = [x.strip() for x in sys.stdin.readlines()]
trees = [[int(num) for num in x] for x in input]

def visible(x: int, y: int) -> bool:
    height = trees[y][x]
    visible = True
    if x == 0 or x == len(trees[0])-1 or y == 0 or y == len(trees)-1:
        return visible
    # top text
    for j in range(y-1, -1, -1):
        if trees[j][x] >= height:
            visible = False
    if visible:
        return visible
    visible = True
    # bottom text
    for j in range(y+1, len(trees)):
        if trees[j][x] >= height:
            visible = False
    if visible:
        return visible
    visible = True
    # left text
    for i in range(x-1, -1, -1):
        if trees[y][i] >= height:
            visible = False
    if visible:
        return visible
    visible = True
    # right text
    for i in range(x+1, len(trees[0])):
        if trees[y][i] >= height:
            visible = False
    
    return visible

def scenic_score(x: int, y: int) -> int:
    height = trees[y][x]
    # top text
    score1 = 0
    for j in range(y-1, -1, -1):
        score1 += 1
        if trees[j][x] >= height:
            break
    # bottom text
    score2 = 0
    for j in range(y+1, len(trees)):
        score2 += 1
        if trees[j][x] >= height:
            break
    # left text
    score3 = 0
    for i in range(x-1, -1, -1):
        score3 += 1
        if trees[y][i] >= height:
            break
    # right text
    score4 = 0
    for i in range(x+1, len(trees[0])):
        score4 += 1
        if trees[y][i] >= height:
            break
    
    return score1*score2*score3*score4

count = 0
for i in range(len(trees)):
    for j in range(len(trees[i])):
        if visible(i, j):
            count += 1

print(f'part 1: {count}')
print(f'part 2: {max([scenic_score(i, j) for i in range(len(trees)) for j in range(len(trees[0]))])}')
