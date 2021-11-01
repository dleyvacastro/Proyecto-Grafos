import json
from jikanpy import Jikan
from igraph import *
from DJ import Dijkstra
from gui import GUI
from FW import FW, import_FWmatrix
import pandas as pd

# Lectura del JSON
animes_json = open('animes.json', 'r')
animes = json.load(animes_json)
animes_json.close()

# Funciones de ponderacion


def g_f(GE_a, GE_b):
    if len(GE_a)+len(GE_b) == 0:
        return 0
    return len(list(set(GE_a) & set(GE_b))) / \
        len(list(set().union(GE_a, GE_b)))


def s_f(SE_a, SE_b):
    if len(SE_a) + len(SE_b) == 0:
        return 0
    return len(list(set(SE_a) & set(SE_b))) / \
        len(list(set().union(SE_a, SE_b)))


def f(g, s): return (1 - (0.7*g + 0.3*s))


def main():
    # Instancias del API
    jikan = Jikan()
   #  anime = jikan.anime(int(input("Ingrese el id del anime que vio: ")))
    # Creacion del grafo
    t4graph = []
    t4graph2 = []
    names = []

    print("Creando el Grafo")
    for cont in range(len(animes)):
        i = animes[cont]
        names.append(i["name"])
        for j in animes[cont+1:]:
            if i != j:
                g_ij = g_f(i["GE"], j["GE"])
                s_ij = s_f(i["SE"], j["SE"])
                f_ij = f(g_ij, s_ij)
                if f_ij < 1:
                    t4graph.append((i["name"], j["name"], round(f_ij, 4)))
                    t4graph2.append((i["name"], j["name"]))

                    # non_related.append((i["name"], j["name"]))

    grafo = Graph.TupleList(t4graph, weights=True)
    grafo.vs["label"] = grafo.vs["name"]
    grafo.es["label"] = grafo.es["weight"]
    print("Grafo Creado")

    df = FW(names, t4graph, t4graph2)
    # df = import_FWmatrix()
    # print(df)

    # algoritmo de Dijkstra
    #Dijkstra(grafo, anime["title"], jikan.anime(42361)["title"])

    """ Impresion en consola
    recomendaciones = df.nsmallest(11, [anime["title"]])
    recomendaciones = recomendaciones['anime'][1:]

    print(f'Porque viste {anime["title"]} Te recomendamos: ')
    print(recomendaciones.to_string(index=False))

    recomendaciones = recomendaciones.values.tolist()
    for i in recomendaciones:
        Dijkstra(grafo, anime["title"], i)
    """
#    # Grafica
    # layout = grafo.layout("kk")
    # plot(grafo, layout=layout)
    GUI(jikan, df)


if __name__ == '__main__':
    main()
