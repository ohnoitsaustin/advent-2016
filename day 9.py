import re


def decompress(compressed_input: str) -> str:
    output = ''
    while compressed_input != '':
        repeat_marker = re.search('\((\d+)x(\d+)\)', compressed_input)
        if(repeat_marker):
            length = int(repeat_marker.group(1))
            repeat = int(repeat_marker.group(2))
            start_splice = repeat_marker.start()
            end_splice = repeat_marker.end()

            output += compressed_input[:start_splice]
            output += compressed_input[end_splice:end_splice+length] * repeat

            compressed_input = compressed_input[end_splice + length:]
        else:
            output += compressed_input
            compressed_input = ''

    return output


tests = '''ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY'''

test_lengths = [len(decompress(test)) for test in tests.split('\n')]
print(test_lengths)
print([6, 7, 9, 11, 6, 18])


puzzle_input = open('day 9 input.txt', 'r').read()
print(len(decompress(puzzle_input)))