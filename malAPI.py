from jikanpy import Jikan
import json
import signal

# Objeto del API Jikan
jikan = Jikan()


def handler(signum, frame):
    # Funcion para definir un timeout de otras funciones
    raise Exception("end of time")


def get_season_animes(year: int, season: str):
    season_data = jikan.season(year=year, season=season)
    season_animes = season_data["anime"]
    ids = []
    for i in season_animes:
        ids.append(i["mal_id"])
    return ids


def add_anime_to_list():
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
    return {"name": anime["title"], "GE": genres2list(anime), "SE": seiyuufilter(a_id)}


def animes2JSON(id_list):
    # Input: Diccionario con el formato definido en la funcion anime2dict
    # Output: None. Creacion del archivo JSON animes.json
    signal.signal(signal.SIGALRM, handler)
    animes = []
    signal.alarm(10)
    for i in id_list:
        try:
            print(i)
            animes.append(anime2dict(i))
        except:
            print("saltado")
            pass
    new_json = open("animes.json", "w")
    new_json.write(json.dumps(animes, indent=4))
    new_json.close()


# cowboy_bebop = jikan.anime(1, extension="characters_staff")
# search_result = jikan.search('anime', 'Hunter x Hunter (2011)')
# print(search_result["results"][0])

# animes2JSON(add_anime_to_list())
# animes2JSON([41587, 42249, 41025, 42361, 40938, 41457, 46095, 41623, 42938, 41456, 40586, 41488, 46102, 42205, 43007, 41402, 41103, 44276, 40174, 42192, 43325, 40729, 43439, 42826, 42590, 41265, 40870, 42395, 47250, 40685, 43756, 40752, 42307, 43229, 40526, 47391, 42774, 42568, 47591, 47639, 43763, 45665, 42516, 42321, 42071, 45587, 45618, 48365, 48442, 48391, 44273, 46381, 46652, 42870, 43778, 42068, 44848, 48770, 48517, 48486, 48790, 48789, 48539, 21, 34566, 41491, 235, 37984, 966, 40682, 40351, 40906, 41074, 40964, 8687, 40145, 41556, 23539, 44191, 2406, 1199, 40129, 6149, 45782, 44056, 1960, 32353, 42653, 40880, 4459, 33398, 37096, 45207, 35478, 42295, 42482, 30151, 7505, 10506, 32956, 8336, 35694, 43416, 18941, 38776, 22669, 30119, 41638,
#            29375, 41384, 29421, 35697, 35696, 35372, 36506, 35698, 35695, 34990, 38099, 38451, 41276, 41458, 48250, 48262, 49920, 43692, 44942, 44074, 43697, 48590, 49236, 43591, 39728, 49200, 37346, 48727, 48735, 49066, 47904, 48481, 49501, 41221, 47405, 49215, 48537, 49063, 42178, 42359, 44068, 49214, 48455, 48953, 48684, 48555, 44041, 48610, 48956, 41918, 48845, 49430, 44090, 48791, 48890, 48942, 49170, 49305, 49098, 48864, 48866, 49118, 44209, 48873, 48844, 49274, 49975, 49615, 43609, 44983, 48468, 36889, 48626, 48697, 48513, 48651, 48889, 48654, 48422, 48652, 48843, 38086, 35759, 37765, 39764, 42798, 48612, 41780, 40664, 41361, 41781, 40554, 45620, 41028, 45654, 48130, 48614, 49235, 49318, 45604, 49241, 49026, 46587, 49228, 37290, 49755, 49060])
animes2JSON(get_season_animes(2021, "spring"))
# nimes2JSON([38000, 21])
# 136
