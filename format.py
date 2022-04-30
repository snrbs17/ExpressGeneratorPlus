import sys

from numpy import array


def formatter(file):
    with open(file, 'r', newline='') as fileReader:
        lines = fileReader.readlines()
    with open(file, 'w') as fileWriter:
        for line in lines:
            if 'require' in line:
                fileWriter.write(require2import(line))
            else:
                fileWriter.write(line)

    return file


def require2import(sentence):
    sentence = sentence.split(' ')
    name = sentence[1]
    source = sentence[3].split("\'")[1]
    return f"import {name} from '{source}'"


if __name__ == "__main__":
    file = sys.argv[1]
    print(formatter(file))
