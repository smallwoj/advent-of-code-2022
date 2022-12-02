import sys
input = sys.stdin.readlines()
guide = [round.strip().split(' ') for round in input]
score = 0
player_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
player_reverse_dict = {
    1: 'X',
    2: 'Y',
    3: 'Z',
}
enemy_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
}
for enemy, player in guide:
    enemy = enemy_dict[enemy]
    player = player_dict[player]
    score += player
    
    if player == enemy:
        score += 3
    elif (enemy) % 3 + 1 == player:
        score += 6

print(f'part 1: {score}')
score = 0

for enemy, player in guide:
    if player == 'Y':
        player = player_reverse_dict[enemy_dict[enemy]]
    elif player == 'Z':
        player = (enemy_dict[enemy]) % 3 + 1
        player = player_reverse_dict[player]
    else:
        if (player := enemy_dict[enemy] - 1) == 0:
            player = 3
        player = player_reverse_dict[player]
    enemy = enemy_dict[enemy]
    player = player_dict[player]
    score += player
    
    if player == enemy:
        score += 3
    elif (enemy) % 3 + 1 == player:
        score += 6
print(f'part 2: {score}')
