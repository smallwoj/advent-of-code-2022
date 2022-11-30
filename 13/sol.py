import sys, functools
from typing import Union
input = sys.stdin.read()


def compare(left: Union[int, list], right: Union[int, list]) -> int:
    if type(left) == type(right) == int:
        cmp = right - left
        return cmp / abs(cmp) if cmp else 0 
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == type(right) == list:
        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return 1
            elif i >= len(right):
                return -1
            else:
                res = compare(left[i], right[i])
                if res != 0:
                    return res / abs(res)
        return 0

sum = 0

total_list = []

for i, raw_pair in enumerate(input.split('\n\n')):
    left, right = raw_pair.split('\n')
    left = eval(left)
    right = eval(right)
    if compare(left, right) > 0:
        sum += i+1
    total_list.extend([left, right])

print(f'part 1: {sum}')

total_list.append([[2]])
total_list.append([[6]])
total_list.sort(key=functools.cmp_to_key(compare), reverse=True)

print(f'part 2: {(total_list.index([[2]]) + 1) * (total_list.index([[6]]) + 1)}')
