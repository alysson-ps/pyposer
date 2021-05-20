import json


def execCmd(cmd):
    with open('pyposer.json', 'r+') as f:
        pyposer = json.load(f)
        return pyposer['scripts'][cmd]
