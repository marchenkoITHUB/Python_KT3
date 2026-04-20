# №1
import re
from toolz import curry, compose_left

splitRegex = curry(re.split)
mapF = curry(map)
filterF = curry(filter)
def readFile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().strip()

def castTypes(row):
    return [row[0], row[1], row[2], int(row[3]), float(row[4])]


def getBooks(yFile):
    res = compose_left(readFile, splitRegex(r'\n'), lambda lines: lines[1:], mapF(splitRegex(r'\|')), mapF(castTypes),list)
    return res(yFile)



result = getBooks("books.csv")
print(result[0])

################################################################################

# №2
# [ ['isbn', 'title', 'author', quantity, price], [...], ... ]

def reformatRow(row):
    return [row[0],f"{row[1]}, {row[2]}", row[3], row[4]]


@curry
def searchIn(word, row):
  return word.lower() in row[1].lower()


def getSecondBooks(yList, word):
  newList = compose_left(filterF(searchIn(word)), mapF(reformatRow), list)
  return newList(yList)

result2 = getSecondBooks(result, 'pYtHoN')
print(result2)

################################################################################

# №3

# ("isbn", quantity*price)

def reformatTuple(row):
    return (row[0], row[2] * row[3])



def toTuple(yList):
  newList = compose_left(mapF(reformatTuple), list)
  return newList(yList)


result3 = toTuple(result2)
print(result3)
