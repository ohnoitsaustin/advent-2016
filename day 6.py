from collections import Counter
puzzleInput = open('day 6 input.txt', 'r').read().split('\n')
answer = ''
for i in range(0, len(puzzleInput[0])-1):
    charInput = [line[i] for line in puzzleInput]

    charFrequency = Counter(charInput)
    mostCommon,count = Counter.most_common(1)
    print(mostCommon)
    answer = answer + mostCommon

print(answer)