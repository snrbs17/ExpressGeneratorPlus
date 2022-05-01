import sys


def jsonParse(file):
    print('jsonParse', file)
    insertScript(file)


def insertScript(file):
    print('insert', file)


if __name__ == "__main__":
    file = sys.argv[1] + '/package.json'
    jsonParse(file)
