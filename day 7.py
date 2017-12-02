from typing import List
import re


def get_rows(txt: str) -> List[str]:
    return txt.split('\n')


def containsABBA(txt: str) -> bool:
    return re.search(r"([a-z])(?!\1)([a-z])\2\1", txt) is not None


def findABA(txt: str) -> str:
    print(re.findall(r"([a-z])([a-z])\1", txt))
    return re.findall(r"([a-z])([a-z])\1", txt)


def textInBrackets(txt: str) -> str:
    return ''.join(re.findall('\[[a-z]+\]', txt))


def textOutsideBrackets(txt: str) -> str:
    return re.sub('\[[a-z]+\]', '', txt)


def supportsTLS(address: str) -> bool:
    return containsABBA(address) and not containsABBA(textInBrackets(address))


def supportsSSL(address: str) -> bool:
    abas = findABA(address)
    return


tests = '''abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn'''
expectedResults = [True, False, False, True]
results = [supportsTLS(test) for test in get_rows(tests)]
print(expectedResults)
print(results)


puzzle_input = open('day 7 input.txt', 'r').read()
addresses = get_rows(puzzle_input)
print(len([address for address in addresses if supportsTLS(address)]))


tests = '''aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb'''
expectedResults = [True, False, True, True]
print(tests)
addresses = get_rows(tests)
print([address for address in addresses if (supportsSSL(address))])