import sys
input = sys.stdin.read()

raw_crates, procedure = input.split('\n\n')
crates = []

def generate_crates(raw_crates):
    raw_crates = raw_crates.split('\n')
    num_stacks = len(raw_crates.pop().split())

    crates = [[] for _ in range(num_stacks)]

    for line in reversed(raw_crates):
        for i in range(0, num_stacks*4, 4):
            if line[i+1] != ' ':
                crates[i//4].append(line[i+1])
    return crates

crates = generate_crates(raw_crates)

for command in procedure.split('\n'):
    command = command.split()
    amount, stack_from, stack_to = map(int, command[1::2])
    while amount:
        crates[stack_to - 1].append(crates[stack_from - 1].pop())
        amount -= 1
    

print('part 1: ', end='')
for crate in crates:
    print(crate[-1], end='')
print()

crates = generate_crates(raw_crates)

for command in procedure.split('\n'):
    command = command.split()
    amount, stack_from, stack_to = map(int, command[1::2])
    to_add = []
    while amount:
        to_add.append(crates[stack_from - 1].pop())
        amount -= 1

    for c in reversed(to_add):
        crates[stack_to - 1].append(c)

print('part 2: ', end='')
for crate in crates:
    print(crate[-1], end='')
print()
