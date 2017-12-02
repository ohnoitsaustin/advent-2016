def isPossible(sides):
    a, b, c = sides
    return a+b > c and b+c > a and c+a > b

puzzleInput = open('day3input.txt', 'r').read()
triangles = puzzleInput.split('\n')
impossibleTriangles = [isPossible((int(side) for side in t.split())) for t in triangles]

from collections import Counter
print(Counter(impossibleTriangles))
