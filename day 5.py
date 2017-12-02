import hashlib

def md5(stringToHash: str):
    return hashlib.md5(stringToHash.encode('utf-8')).hexdigest()

def generateAnswer2(puzzleInput: str) -> str:
    i = 0
    answer = [c for c in "-" * 8]
    while ("-" in answer):
        hash = md5(puzzleInput + str(i))

        if (hash[:5] == '00000'):
            print(hash)
            pos = hash[5]
            value = hash[6]
            if (pos.isdigit() and int(pos) < 8 and answer[int(pos)] == '-'):
                answer[int(pos)] = value

        i += 1

    return ''.join(answer)

def generateAnswer1(puzzleInput: str) -> str:
    i = 0
    answer = ''
    while (len(answer) < 8):
        hash = md5(puzzleInput + str(i))

        if (hash[:5] == '00000'):
            print(hash)
            answer = answer + hash[5]

        i += 1

    return answer


puzzleInput: str = "ffykfhsq"
answer = generateAnswer2(puzzleInput)
print(answer)