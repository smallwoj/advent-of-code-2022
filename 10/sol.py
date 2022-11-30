import sys
input = [s.strip() for s in sys.stdin.readlines()]

X = 1
curr_i = ''
curr_c = 0
c_left = 0
task_queue = [x for x in reversed(input)]
cycle_times = {
    'noop': 1,
    'addx': 2,
}
sum = 0
screen = []
crt_row = ''

while task_queue or c_left or curr_i:
    curr_c += 1
    if not curr_i:
        curr_i = task_queue.pop()
        c_left = cycle_times[curr_i.split()[0]]

    if (curr_c - 20) % 40 == 0:
        sum += curr_c * X
    
    if curr_c % 40 in range(X, X+3):
        crt_row += '#'
    else:
        crt_row += '.'
    
    if curr_c % 40 == 0 and curr_c != 0:
        screen.append(crt_row)
        crt_row = ''

    c_left -= 1
    if c_left <= 0:
        if curr_i.split()[0] == 'addx':
            X += int(curr_i.split()[-1])
        curr_i = ''
print(f'part 1: {sum}')
print('part 2:')
for r in screen:
    print(r)
    