# The (minimalistic) custom database for this project

import json
import os

class SimpleDB:
    def __init__(self, name: str):
        self.name = name
        self.filename = name + ".json"

        if self.filename not in os.listdir():
            with open(self.filename, "w") as f:
                f.write("{}")
    
    def insert(self, key, value):
        # Add a new key
        db = json.load(open(self.filename, "r"))
        db[key] = value
        json.dump(db, open(self.filename, "w"))
        del db

    def set(self, key, value):
        # basically the same as insert, but other name
        self.insert(key, value)
    
    def get(self):
        # Get the whole DB as a dict
        return json.load(open(self.filename, "r"))

    def getkeys(self):
        # Get the all the DB's keys as a list
        return list(json.load(open(self.filename, "r")).keys())