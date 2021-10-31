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
def get_path(L, u, z, r=[]):
    lz = L[z][1]
    r.append(lz[-1])
    if u in r:
        return r
    return get_path(L, u, lz[-1], r)


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

    L = {i: [float('inf'), []] for i in G.vs["name"]}
    L[u] = [0, []]
    S = []

    while z not in S:
        L_S = {i: L[i][0] for i in L if i not in S}
        x = min(L_S, key=L_S.get)
        # for i in minimums(L):
        #    if i not in S:
        #        x = i
        #        print(x)
        #        # ime.sleep(0.5)
        #        break

        S = list(set().union(S, [x]))
        # print(L)
        for v in G.vs["name"]:
            # print(v)
            if v not in S:
                if L[v][0] < L[x][0] + w(G, x, v):
                    L[v] = [L[v][0], L[v][1]]
                else:
                    L[v][1].append(x)
                    L[v] = [L[x][0] + w(G, x, v), L[v][1]]
                # L[v] = min(L[v], L[x] + w(G, x, v))
    path = get_path(L, u, z, [])
    path = path[::-1]
    path.append(z)
    if L[z][0] == float('inf'):
        path = []
    print(f'{u} -- {z}: {path} w = {L[z][0]}')
    return L
