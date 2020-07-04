import json
class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year

tournaments = {
    "AeroOpen": 2010,
    "WWE": 2019,
    "FIDE GRAND PRIX": 2016,
}

json_data = json.dumps(tournaments, indent=2)

loaded = json.loads(json_data)
print(loaded)