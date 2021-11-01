import PySimpleGUI as sg
from jikanpy import Jikan
import json
from igraph import *
from DJ import Dijkstra
from FW import FW, import_FWmatrix
import pandas as pd

# Lectura del JSON
animes_json = open('animes.json', 'r')
animes = json.load(animes_json)
animes_json.close()


jikan = Jikan()
# Creacion del grafo
# FWmatrix = FW(names, t4graph, t4graph2)
df = import_FWmatrix()

# for i in recomendaciones:
#    Dijkstra(grafo, anime["title"], i)


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Ingrese el mal_id del anime que vio:')],
          [sg.Text('mal_id: '), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Anime Suggester', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    anime = jikan.anime(values[0])["title"]
    recomendaciones = df.nsmallest(11, [anime])
    print(recomendaciones)

    recomendaciones = recomendaciones['anime'][1:]
    recomendaciones = recomendaciones.values.tolist()

    vis_recomendaciones = [
        [sg.Text(f'{i+1}. {recomendaciones[i]}')] for i in range(len(recomendaciones))]
    layout = [
        [sg.Text(text=f'Porque viste {anime} te recomendamos:')]
    ] + vis_recomendaciones
    window = sg.Window('Window Title', layout)


window.close()
