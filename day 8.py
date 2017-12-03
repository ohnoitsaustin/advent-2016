from typing import List

Screen = List[List[str]]


def rotate_list(l, n):
    return l[-n:] + l[:-n]


def screen_output(screen: Screen) -> str:
    return '\n'.join([''.join(row) for row in screen])


def rect(screen: Screen, x: int, y: int) -> Screen:
    for i in range(0,y):
        for j in range(0,x):
            screen[i][j] = '#'
    return screen


def rotate_row(screen: Screen, y: int, amount: int) -> Screen:
    screen[y] = rotate_list(screen[y], amount)
    return screen


def rotate_column(screen: Screen, x: int, amount: int) -> Screen:
    column = [row[x] for row in screen]
    column = rotate_list(column, amount)
    for i, row in enumerate(screen):
        screen[i][x] = column[i]
    return screen


def rotate(screen: Screen, axis: str, index: int, amount: int) -> Screen:
    rotate_functions = {'row': rotate_row, 'column': rotate_column}
    return rotate_functions[axis](screen, index, amount)

puzzle_input = open('day 8 input.txt', 'r').read()
instructions = puzzle_input.split("\n")
screen = [[' ' for i in range(50)] for i in range(6)]

for instruction in instructions:
    instruction_parts = instruction.split()
    if instruction_parts[0] == 'rect':
        x,y = instruction_parts[1].split('x')
        screen = rect(screen, int(x), int(y))
    if instruction_parts[0] == 'rotate':
        axis = instruction_parts[1]
        index = int(instruction_parts[2][2:])
        amount = int(instruction_parts[4])
        screen = rotate(screen, axis, index, amount)

print(screen_output(screen))
print(sum([1 for row in screen for col in row if col == '#']))

# ZJHRKCPLYJ