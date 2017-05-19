import json
from pprint import pprint
import pickle
##add try catch blocks for files.
def loadStates(filename):
    data = {}
    with open(filename) as data_file:
        data = json.load(data_file)

    return data["states"]
