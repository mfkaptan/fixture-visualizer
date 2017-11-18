import json
from collections import OrderedDict

TEAMS = OrderedDict([
    ("Galatasaray", 1),
    ("Başakşehir", 2),
    ("Kayserispor", 3),
    ("Beşiktaş", 4),
    ("Bursaspor", 5),
    ("Fenerbahçe", 6),
    ("Göztepe", 7),
    ("Akhisarspor", 8),
    ("Sivasspor", 9),
    ("Alanyaspor", 10),
    ("Malatyaspor", 11),
    ("Trabzonspor", 12),
    ("Kasımpaşa", 13),
    ("Antalyaspor", 14),
    ("Konyaspor", 15),
    ("Karabükspor",16),
    ("Osmanlıspor",17),
    ("Gençlerbirliği",18)
])

MATCHES = {}

def get_other(t, title):
    t1, t2 = title.split("-")
    if t in t1:
        return get_team(t2)
    return get_team(t1)

def get_team(t):
    for team in TEAMS:
        if team in t:
            return team

def main():
    with open("splig.json", "r") as sp:
        cal = OrderedDict(json.loads(sp.read()))["calendars"][0]["events"]

    for t in TEAMS:
        MATCHES[t] = []

        for i in cal:
            if t in i["summary"]:
                MATCHES[t].append(TEAMS[get_other(t, i["summary"])])

        print(t)
        print("11 hafta:" , MATCHES[t][:11], sum(MATCHES[t][:11]))
        print("Kalan:", MATCHES[t][11:17], sum(MATCHES[t][11:17]))
        print()

if __name__ == "__main__":
    main()
