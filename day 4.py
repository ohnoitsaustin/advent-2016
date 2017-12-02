from collections import Counter

puzzleInput = open('day 4 input.txt', 'r').read().split('\n')

def tokenizeRoomString(room: str):
    roomParts = room.split('-')
    sectorAndChecksum = roomParts[-1].split('[')
    sector = int(sectorAndChecksum[0])
    checksum = sectorAndChecksum[1][:-1]
    room = '-'.join(roomParts[:-1])

    return room, sector, checksum

def getSector(room: str):
    room, sector, checksum = tokenizeRoomString(room)

    return sector

def isValidRoom(room: str):
    room, sector, checksum = tokenizeRoomString(room)
    room = room.replace('-', '')
    letters = sorted(list(room))
    topFive = ''.join([letter for letter,count in Counter(letters).most_common(5)])
    return topFive == checksum

sectors = [getSector(room) for room in puzzleInput if isValidRoom(room)]
print(sum(sectors))