import json
from jikanpy import Jikan
from igraph import *
from DJ2 import Dijkstra
from FW import FW
import pandas as pd

# Lectura del JSON
animes = open('animes.json', 'r')
animes = json.load(animes)

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


def f(g, s): return (1 - (0.5*g + 0.5*s))


def main():
    jikan = Jikan()
    anime = jikan.anime(11061)
    # Creacion del grafo
    t4graph = []
    t4graph2 = []
    names = []

    for cont in range(len(animes)):
        i = animes[cont]
        names.append(i["name"])
        for j in animes[cont+1:]:
            if i != j:
                g_ij = g_f(i["GE"], j["GE"])
                s_ij = s_f(i["SE"], j["SE"])
                f_ij = f(g_ij, s_ij)
                if f_ij != 1:
                    t4graph.append((i["name"], j["name"], round(f_ij, 4)))
                    t4graph2.append((i["name"], j["name"]))

                    #non_related.append((i["name"], j["name"]))

    grafo = Graph.TupleList(t4graph, weights=True)
    grafo.vs["label"] = names
    grafo.es["label"] = grafo.es["weight"]

    # for i in non_related:
    #    grafo.delete_edges([i])

    # print(names)
    # print(t4graph)
    # print(t4graph2)
    FWmatrix = FW(names, t4graph, t4graph2)
    Dijkstra(grafo, anime["title"], jikan.anime(42361)["title"])
    # print(FWmatrix)
    df = pd.DataFrame(FWmatrix)
    df.insert(0, "anime", names)
    df = df.rename(columns={i: names[i] for i in range(len(names))})
    recomendaciones = df.nsmallest(11, [anime["title"]])
    recomendaciones = recomendaciones['anime'][1:]
    print(recomendaciones)
    df.to_excel('FWmatrix.xlsx', index=False)
#    # Grafica
    layout = grafo.layout("kk")
    plot(grafo, layout=layout)
   # print(grafo)


if __name__ == '__main__':
    main()
