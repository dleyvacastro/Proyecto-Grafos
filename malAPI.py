from jikanpy import Jikan
import json

jikan = Jikan()


def purge_non_main_characters(l):
    nl = []
    for i in l:
        if i["role"] == "Main":
            nl.append(i)
    return nl

def seiyuufilter(a_id):
    seiyuus = []
    anime_characters = jikan.anime(a_id, extension="characters_staff")
    main_characters = purge_non_main_characters(anime_characters["characters"])
    for i in main_characters:
        va_i = i["voice_actors"]
        for j in va_i:
            if j["language"] == "Japanese":
                seiyuus.append(j["name"])
                break
    return seiyuus
    # new_json = open("cowboy_bebop.json", 'w')
    # new_json.write(y)
    # new_json.close()

def genres2list(anime):
    genres = []
    for i in anime["genres"]:
        genres.append(i["name"])
    return genres

def anime2dict(a_id):
    anime = jikan.anime(a_id)
    return {"name": anime["title"], "GE" : genres2list(anime), "SE" : seiyuufilter(a_id)}

def animes2JSON(id_list):
    animes = []
    for i in id_list:
        animes.append(anime2dict(i))
    new_json = open("animes2.json", "w")
    new_json.write(json.dumps(animes, indent=4))
    new_json.close()

    
#cowboy_bebop = jikan.anime(1, extension="characters_staff")
# search_result = jikan.search('anime', 'Hunter x Hunter (2011)')
# print(search_result["results"][0])

animes2JSON([16498, 33486, 11061])
# 136