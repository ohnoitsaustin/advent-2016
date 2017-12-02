myLocation = (0, 0, 0)


def calculateDirection(direction, turnDirection):
    # turnDirection should be 0 (left) or 1 (right)
    direction = direction + 1 if turnDirection else direction - 1
    if (direction == -1):
        direction = 3
    if (direction == 4):
        direction = 0
    return direction


def fwd(x, dis):
    return x + dis


def back(x, dis):
    return x - dis


def move(location, instruction):
    (x, y, direction) = location
    (turnDirection, distance) = instruction

    direction = calculateDirection(direction, turnDirection)

    if (direction % 2):
        x = fwd(x, distance) if direction == 1 else back(x, distance)
    else:
        y = fwd(y, distance) if direction == 0 else back(y, distance)

    return (x, y, direction)


def decode(string):
    direction = 0 if string[:1] == 'L' else 1
    distance = int(string[1:])
    return (direction, distance)


adventInput = "R4, R1, L2, R1, L1, L1, R1, L5, R1, R5, L2, R3, L3, L4, R4, R4, R3, L5, L1, R5, R3, L4, R1, R5, L1, R3, L2, R3, R1, L4, L1, R1, L1, L5, R1, L2, R2, L3, L5, R1, R5, L1, R188, L3, R2, R52, R5, L3, R79, L1, R5, R186, R2, R1, L3, L5, L2, R2, R4, R5, R5, L5, L4, R5, R3, L4, R4, L4, L4, R5, L4, L3, L1, L4, R1, R2, L5, R3, L4, R3, L3, L5, R1, R1, L3, R2, R1, R2, R2, L4, R5, R1, R3, R2, L2, L2, L1, R2, L1, L3, R5, R1, R4, R5, R2, R2, R4, R4, R1, L3, R4, L2, R2, R1, R3, L5, R5, R2, R5, L1, R2, R4, L1, R5, L3, L3, R1, L4, R2, L2, R1, L1, R4, R3, L2, L3, R3, L2, R1, L4, R5, L1, R5, L2, L1, L5, L2, L5, L2, L4, L2, R3"
instructions = adventInput.split(", ")
log = []
for instruction in instructions:
    x, y, d = myLocation
    log.append((x, y))
    myLocation = move(myLocation, decode(instruction))

x, y, direction = myLocation
distance = abs(x) + abs(y)
print(distance)