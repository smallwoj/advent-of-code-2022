import sys
input = sys.stdin.read()

monkeys = []
for raw_monkey in input.split('\n\n'):
    raw_monkey = raw_monkey.split('\n')
    monkey = {}
    monkey['items'] = [int(x) for x in raw_monkey[1].split(': ')[-1].split(', ')]
    monkey['operation'] = raw_monkey[2].split(': ')[-1].split('= ')[-1]
    monkey['test'] = int(raw_monkey[3].split()[-1])
    monkey[True] = int(raw_monkey[4].split()[-1])
    monkey[False] = int(raw_monkey[5].split()[-1])
    monkey['inspected'] = 0
    monkeys.append(monkey)
new = 0

for round in range(20):
    for monkey in monkeys:
        while monkey['items']:
            item = monkey['items'].pop(0)
            old = item
            new = eval(monkey['operation'])
            new //= 3
            monkeys[monkey[new % monkey['test'] == 0]]['items'].append(new)
            monkey['inspected'] += 1

sorted_monkeys = sorted(monkeys, key=lambda x: x['inspected'], reverse=True)
print(f"part 1: {sorted_monkeys[0]['inspected'] * sorted_monkeys[1]['inspected']}")

monkeys = []
for raw_monkey in input.split('\n\n'):
    raw_monkey = raw_monkey.split('\n')
    monkey = {}
    monkey['items'] = [int(x) for x in raw_monkey[1].split(': ')[-1].split(', ')]
    monkey['operation'] = raw_monkey[2].split(': ')[-1].split('= ')[-1]
    monkey['test'] = int(raw_monkey[3].split()[-1])
    monkey[True] = int(raw_monkey[4].split()[-1])
    monkey[False] = int(raw_monkey[5].split()[-1])
    monkey['inspected'] = 0
    monkeys.append(monkey)

the_big_one = 1
for m in monkeys:
    the_big_one *= m['test']

for round in range(10000):
    for monkey in monkeys:
        while monkey['items']:
            item = monkey['items'].pop(0)
            old = item
            new = eval(monkey['operation'])
            new %= the_big_one
            monkeys[monkey[new % monkey['test'] == 0]]['items'].append(new)
            monkey['inspected'] += 1

sorted_monkeys = sorted(monkeys, key=lambda x: x['inspected'], reverse=True)
print(f"part 2: {sorted_monkeys[0]['inspected'] * sorted_monkeys[1]['inspected']}")
