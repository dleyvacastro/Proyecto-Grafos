import json
from igraph import *

# Lectura del JSON
animes = open('animes2.json', 'r')
animes = json.load(animes)

# Funciones de ponderacion


def g_f(GE_a, GE_b): return len(list(set(GE_a) & set(GE_b))) / \
    len(list(set().union(GE_a, GE_b)))


def s_f(SE_a, SE_b): return len(list(set(SE_a) & set(SE_b))) / \
    len(list(set().union(SE_a, SE_b)))


def f(g, s): return 1 - (0.5*g + 0.5*s)


# Creacion del grafo
t4graph = []
t4graph2 = []
names = []
non_related = []
# g = Graph()

for cont in range(len(animes)):
    i = animes[cont]
    names.append(i["name"])
    print(i)
    for j in animes[cont+1:]:
        if i != j:
            g_ij = g_f(i["GE"], j["GE"])
            s_ij = s_f(i["SE"], j["SE"])
            f_ij = f(g_ij, s_ij)
            t4graph.append((i["name"], j["name"], round(f_ij, 4)))
            t4graph2.append((i["name"], j["name"]))
            if f_ij == 1:
                non_related.append((i["name"], j["name"]))

grafo = Graph.TupleList(t4graph, weights=True)
grafo.vs["label"] = names
grafo.es["label"] = grafo.es["weight"]

for i in non_related:
    grafo.delete_edges([i])

# Grafica
layout = grafo.layout("kk")
plot(grafo, layout=layout)
print(grafo)
