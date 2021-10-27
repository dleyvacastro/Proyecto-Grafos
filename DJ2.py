from igraph import *


# def minimums(some_dict):
#    # Tomada de Stackoverflow
#    positions = []  # output variable
#    min_value = float("inf")
#    for k, v in some_dict.items():
#        if v == min_value:
#            positions.append(k)
#        if v < min_value:
#            min_value = v
#            positions = []  # output variable
#            positions.append(k)
#
#    return positions


def w(G, x, v):
    try:
        return G.es[G.get_eid(x, v)]["weight"]
    except:
        return float('inf')


def Dijkstra(G, u, z):
    # print(list(G.vs()))
    #neis = G.neighbors(u)
    # print(G.vs[neis]["name"])
    #id = G.get_eid("Cowboy Bebop", "One Piece")
    # print(G.es[id]['weight'])

    L = {i: float('inf') for i in G.vs["name"]}
    L[u] = 0
    S = []

    while z not in S:
        L_S = {i: L[i] for i in L if i not in S}
        x = min(L_S, key=L_S.get)
        # for i in minimums(L):
        #    if i not in S:
        #        x = i
        #        print(x)
        #        # ime.sleep(0.5)
        #        break

        S = list(set().union(S, [x]))
        for v in G.vs["name"]:
            if v not in S:
                L[v] = min(L[v], L[x] + w(G, x, v))

    print(f'{u} -- {z}: {L[z]}')
    return S, L
