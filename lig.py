import json
from collections import OrderedDict
from operator import itemgetter

TEAMS = None

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
    global TEAMS, MATCHES

    with open("standings.json", "r") as stand:
        t_dict = json.loads(stand.read())
        TEAMS = OrderedDict((k, t_dict[k]) for k in sorted(t_dict, key=t_dict.get))

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
