import sys

from numpy import array


def formatter(file):
    with open(file, 'r', newline='') as fileReader:
        lines = fileReader.readlines()
    with open(file, 'w') as fileWriter:
        for line in lines:
            if 'require' in line:
                fileWriter.write(require2import(line))
            elif 'module.exports' in line:
                fileWriter.write(export(line))
            else:
                fileWriter.write(line)


def require2import(sentence):
    sentence = sentence.split(' ')
    name = sentence[1]
    source = sentence[-1].split("\'")[1]
    return f"import {name} from '{source}';\n"


def export(sentence):
    sentence = sentence.split(' ')
    name = sentence[-1]
    return f"export default {name}\n"


if __name__ == "__main__":
    file = sys.argv[1]
    formatter(file)
