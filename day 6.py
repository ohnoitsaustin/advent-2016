def most_common(lst):
    return min(set(lst), key=lst.count)


def get_rows(message_input: str):
    return message_input.split("\n")


def common_message(message_input: str):
    answer = ''
    messages = get_rows(message_input)
    for i in range(0, len(messages[0])):
        charInput = [line[i] for line in messages]
        mostCommon = most_common(charInput)
        answer = answer + mostCommon

    return answer


puzzleInput = open('day 6 input.txt', 'r').read()
answer = common_message(puzzleInput)
print(answer)


puzzleInput = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''

answer = common_message(puzzleInput)
print(answer)