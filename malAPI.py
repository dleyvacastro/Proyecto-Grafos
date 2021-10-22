from jikanpy import Jikan
import json


def purge_non_main_characters(l):
    for i in l:
        if i["role"] != "Main":
            l.remove(i)


jikan = Jikan()
cowboy_bebop = jikan.anime(1, extension="characters_staff")

characters = cowboy_bebop["characters"]
y = json.dumps(cowboy_bebop, indent=4)
new_json = open("cowboy_bebop.json", 'w')
new_json.write(y)
new_json.close()
