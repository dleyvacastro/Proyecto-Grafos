from igraph import *
from DJ import Dijkstra
from FW import FW
import pandas as pd

t = [('a', 'b', 4), ('a', 'c', 5),  ('d', 'e', 5)]
# t2 = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]
t2 = [i[:-1] for i in t]

g = Graph.TupleList(t, weights=True)

g.vs["label"] = g.vs["name"]
g.es["label"] = g.es["weight"]

n = ['a', 'b', 'c', 'd', 'e']
FWmatrix = FW(n, t, t2)
print(FWmatrix)
Dijkstra(g, 'a', 'd')

layout = g.layout("kk")
plot(g, layout=layout)
