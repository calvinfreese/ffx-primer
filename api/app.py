from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/monsters/all")
def all_monsters():
    with open('../db/creatures.json') as file:
        data = json.load(file)
        return data
    
@app.route("/monsters/location/<loc>")
def monsters_by_loc(loc):
    found_loc_name = ""
    with open("../db/locations.json") as loc_file:
        loc_data = json.load(loc_file)
        all_locs = loc_data["locations"]
        for location in all_locs:
            if location["slug"] == loc:
                found_loc_name = location["name"]
        print(found_loc_name)

    with open('../db/creatures.json') as file:
        loc_monsters = []
        data = json.load(file)
        creatures = data["creatures"]
        for monster in creatures:
            if monster["location"] == found_loc_name:
                loc_monsters.append(monster)

        return loc_monsters