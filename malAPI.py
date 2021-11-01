from jikanpy import Jikan
import json
import signal

# Objeto del API Jikan
jikan = Jikan()
urls = {}


def handler(signum, frame):
    # Funcion para definir un timeout de otras funciones
    raise Exception("end of time")


def get_season_animes(year: int, season: str):
    season_data = jikan.season(year=year, season=season)
    season_animes = season_data["anime"]
    ids = []
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(10)
    for i in season_animes:
        try:
            print(i["title"])
            ids.append(i["mal_id"])
        except:
            print("Saltado")
    return ids


def get_last_n_years(iy, fy):
    seasons = ['winter', 'spring', 'summer', 'fall']
    ids = []
    for i in range(iy, fy):
        for j in seasons:
            ids = list(set().union(ids, get_season_animes(i, j)))
    return ids


def add_anime_id_to_list():
    # Funcion que recibe por consola diversos mal_id's de animes
    new_json = open("anime_list.json", 'r')
    anime_list = json.load(new_json)
    new_json.close()
    control = int(input('Ingresar animes 1 - Si / 0 - No: '))
    while control:
        control = int(input('Ingrese el mal_id: '))
        if control <= 0:
            break
        anime_list.append(control)
    new_json = open("anime_list.json", 'w')
    new_json.write(json.dumps(anime_list, indent=4))
    new_json.close()
    return list(set(anime_list))


def add_anime_to_list():
    control = int(input('Ingresar animes 1 - Si / 0 -No: '))
    new_animes = []
    with open("animes.json", 'r') as a:
        a_id = json.load(a)
        ids = [i["mal_id"] for i in a_id]
    while control:
        control = int(input('Ingrese el mal_id: '))
        if control <= 0:
            break
        if control not in ids:
            new_animes.append(anime2dict(control))
            ids.append(control)
        else:
            print('Anime ya en la lista.')

    with open("anime_list.json", 'w') as a:
        a.write(json.dumps(ids, indent=4))

    with open("urls.json", 'r') as a:
        old_urls = json.loads(a.read())
    with open("urls.json", 'w') as a:
        a.write(json.dumps(old_urls | urls, indent=4))
    animes_json = open("animes.json", 'r')
    animes = json.load(animes_json)
    animes_json.close()

    with open("animes.json", 'w') as a:
        a.write(json.dumps(animes + new_animes, indent=4))


# def purge_non_main_characters(l):
#    nl = []
#    for i in l:
#        if i["role"] == "Main":
#            nl.append(i)
#    return nl

def seiyuufilter(a_id):
    # Input: int mal_id
    # Output: lista con los seiyuu del anime
    seiyuus = []
    anime_characters = jikan.anime(a_id, extension="characters_staff")
    # main_characters = purge_non_main_characters(anime_characters["characters"])
    for i in anime_characters["characters"]:
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
    # Input: Objeto jikan de un anime en especifico
    # Output: lista con los generos de dicho anime
    genres = []
    for i in anime["genres"]:
        genres.append(i["name"])
    return genres


def anime2dict(a_id):
    # Input: int mal_id
    # Output: diccionario con los generos, interpretes vocales y nombre del anime
    anime = jikan.anime(a_id)
    print(anime["title"])
    urls[anime["title"]] = anime["url"]

    return {"name": anime["title"], "mal_id": anime["mal_id"], "GE": genres2list(anime), "SE": seiyuufilter(a_id)}


def animes2JSON(id_list):
    # Input: Diccionario con el formato definido en la funcion anime2dict
    # Output: None. Creacion del archivo JSON animes.json
    animes = []
    for i in id_list:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        try:
            print(i)
            animes.append(anime2dict(i))
        except:
            print("saltado")
            pass
    with open("urls.json", 'w') as a:
        a.write(json.dumps(urls, indent=4))
    new_json = open("animes.json", "w")
    new_json.write(json.dumps(animes, indent=4))
    new_json.close()


# animes2JSON(add_anime_id_to_list())
add_anime_to_list()
# l = get_last_n_years(2015, 2020)
# Animes de 2015 - 2020
# njson = open("test.json", 'r')
# id_list_2015_2020 = json.load(njson)
# njson.close()
#
# animes2JSON(id_list_2015_2020)
# animes2JSON(get_season_animes(2021, "spring"))
