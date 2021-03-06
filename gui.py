import PySimpleGUI as sg
import json
from jikanpy import Jikan
from DJ import Dijkstra
import pandas as pd
import webbrowser


def inf_filter(d: dict) -> list:
    inf_list = []
    for i in d:
        if d[i] != float('inf'):
            inf_list.append(i)

    return inf_list


def GUI(jikan, df):

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    # Event Loop to process "events" and get the "values" of the inputs
    layout = [
        [sg.Text('Bienvenido a Tactical Anime Suggestor')],
        [sg.Text('Nombre del anime que vió:'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    window = sg.Window('test', layout)
    inicial = 1

    font = ('Raleway', 14, 'underline')
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        with open("anime_list.json", 'r') as a:
            a = json.load(a)
            if inicial:
                q = [i["title"]
                     for i in jikan.search("anime", values[0], page=1)["results"] if i["mal_id"] in a]
                q = q[:10]

                inicial = 0
            elif event in q:
                break

        layout = [[sg.Button(i)] for i in q]
        window = sg.Window('test', layout)

    window.close()
    # Create the Window
    anime = event
    recomendaciones = df.nsmallest(11, [anime])
    # print(recomendaciones)

    valores = recomendaciones[anime][1:]
    valores = valores.values.tolist()
    recomendaciones = recomendaciones['anime'][1:]
    recomendaciones = recomendaciones.values.tolist()

    recomendaciones2 = {recomendaciones[i]: valores[i]
                        for i in range(len(recomendaciones))}

    # print(recomendaciones2)
    recomendaciones = inf_filter(recomendaciones2)
    # print(recomendaciones)
    if recomendaciones:
        with open("urls.json", 'r') as urls:
            urls = json.load(urls)
            vis_recomendaciones = [
                [sg.Text(f'{i+1}. {recomendaciones[i]}', enable_events=True, font=font, key=f"URL {urls[recomendaciones[i]]}")] for i in range(len(recomendaciones))]
        layout = [
            [sg.Text(
                text=f'Porque viste {anime} te recomendamos:', font=('Rubik', 15))]
        ] + vis_recomendaciones

    else:
        layout = [[sg.Text(
            text="404: El anime seleccionado esta aislado", font=('Rubik', 15)
        )]]
    window = sg.Window('Suggestions', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event.startswith("URL "):
            url = event.split(' ')[1]
            webbrowser.open(url)
        # print('You entered ', values[0])

    window.close()
