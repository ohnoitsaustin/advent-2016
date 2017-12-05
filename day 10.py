import re
from typing import List, Dict, Tuple
Bot = Dict[List[int], Dict[Dict[str, int], Dict[str, int]]]

def number_of_bots(puzzle_input: str) -> int:
    bot_string_matches = re.findall('bot ([0-9]+)', puzzle_input)
    return len(set(bot_string_matches))


def number_of_outputs(puzzle_input: str) -> int:
    output_string_matches = re.findall('output ([0-9]+)', puzzle_input)
    return len(set(output_string_matches))


def assign_output(bot, which, r_type, r_index):
    bot['receivers'][which]['type'] = r_type
    bot['receivers'][which]['index'] = r_index
    return bot


def initialize_bots(puzzle_input: str) -> List[Bot]:
    n_bots = number_of_bots(puzzle_input)
    bots = [{
                'values': [],
                'receivers': {
                    'low': {'type': None, 'index': None},
                    'high': {'type': None, 'index': None}
                }
            } for i in range(n_bots)]
    for row in puzzle_input.split('\n'):
        parts = row.split()
        if parts[0] == 'value':
            bot_index = int(parts[-1])
            value = int(parts[1])
            bots[bot_index]['values'].append(value)
        if parts[0] == 'bot':
            i = int(parts[1])
            low_receiver_type = parts[5]
            low_receiver_index = int(parts[6])
            high_receiver_type = parts[10]
            high_receiver_index = int(parts[11])
            bots[i] = assign_output(bots[i], 'low', low_receiver_type, low_receiver_index)
            bots[i] = assign_output(bots[i], 'high', high_receiver_type, high_receiver_index)

    return bots


def any_bot_has_two_numbers(bots: List[Bot]) -> bool:
    return len([bot for bot in bots if len(bot['values'])==2])>0


def redistribute_wealth(bots: List[Bot], outputs: List[int]) -> Tuple[List[Bot], List[int]]:
    for i, bot in enumerate(bots):
        if len(bot['values']) == 2:
            low = min(bot['values'])
            high = max(bot['values'])
            bot['values'] = []
            low_i = bot['receivers']['low']['index']
            high_i = bot['receivers']['high']['index']

            if bot['receivers']['low']['type'] == 'output':
                outputs[low_i] = low
            else:
                bots[low_i]['values'].append(low)

            if bot['receivers']['high']['type'] == 'output':
                outputs[high_i] = high
            else:
                bots[high_i]['values'].append(high)

            if low == 17 and high == 61:
                print(i)

    return bots, outputs


def answer(puzzle_input: str) -> None:
    n_outputs = number_of_outputs(puzzle_input)
    outputs = [-1 for i in range(n_outputs)]

    bots = initialize_bots(puzzle_input)

    while any_bot_has_two_numbers(bots):
        bots, outputs = redistribute_wealth(bots, outputs)

    print(bots)
    print(outputs)
    return


puzzle_input = open('day 10 input.txt', 'r').read()

test = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''

answer(test)

answer(puzzle_input)