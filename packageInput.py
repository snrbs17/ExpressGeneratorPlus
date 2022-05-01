import json
import sys


def jsonParse(file):
    print('jsonParse', file)
    with open(file) as jsonFile:
        jsonData = json.load(jsonFile)
    return jsonData


def insertScript(jsonData):
    if jsonData.get("scripts") == None:
        jsonData.update({"scripts": {}})
    jsonData["scripts"].update(
        {"start": "node ./bin/www.js",
         "dev": "NODE_ENV=development npm-run-all server",
         "server": "babel-nede ./src/bin/www.js"})


def updateFile(file, jsonData):
    with open(file, 'w') as output:
        json.dump(jsonData, output)


if __name__ == "__main__":
    file = sys.argv[1] + '/package.json'
    jsonData = jsonParse(file)
    insertScript(jsonData)
    updateFile(file, jsonData)
