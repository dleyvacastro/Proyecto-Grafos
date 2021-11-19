import numpy as np
import json
import pandas as pd
from datetime import datetime


def FW_a(A, B, C):
    z = len(A)
    W = np.zeros((z, z))

    for i in range(z):
        for j in range(z):
            if (A[i], A[j]) in C:
                m = C.index((A[i], A[j]))
                (W[i])[j] = (B[m])[2]
                (W[j])[i] = (B[m])[2]
            elif (A[j], A[i]) in C:
                m = C.index((A[j], A[i]))
                (W[i])[j] = (B[m])[2]
                (W[j])[i] = (B[m])[2]
        # print(f"W:\n {W}")
    L = np.zeros((z, z))
    for i in range(z):
        for j in range(z):
            if (W[i])[j] != 0:
                (L[i])[j] = (W[i])[j]
                (L[j])[i] = (W[i])[j]
            elif i != j and (W[i])[j] == 0:
                (L[i])[j] = float('inf')
                (L[j])[i] = float('inf')
        # print(f"L: \n {L}")

    L1 = np.zeros((z, z))
    for n in range(z):
        for i in range(z):
            for j in range(z):
                (L1[i])[j] = min((L[i])[j], (L[n])[j] + (L[i])[n])
                (L1[j])[i] = min((L[i])[j], (L[n])[j] + (L[i])[n])

        L = L1
        L1 = np.zeros((z, z))

    return L


def FW(A, B, C):
    # LLamado del algoritmo FW
    t1 = datetime.now()
    print(f"Iniciando Floyd-Warshall: {t1}")
    FWmatrix = FW_a(A, B, C)
    t2 = datetime.now()
    tdelta = t2-t1
    print(f"Fin de FW: {t2}, tiempo empleado: {tdelta}")
    df = pd.DataFrame(FWmatrix)
    df.insert(0, "anime", A)

    df = df.rename(columns={i: A[i] for i in range(len(A))})
    df.to_csv('FWmatrix.csv', index=False)
    print("Excel creado")

    return df


def import_FWmatrix(name='FWmatrix.csv'):
    FWmatrix = pd.read_csv(name)
    return FWmatrix


#A = ['A', 'B', 'C', 'D']
#C = [['A', 'B'], ['A', 'C'], ['A', 'D'],['B', 'D'], ['C', 'D']]
#B = [['A', 'B', 3], ['A', 'C', 4], ['A', 'D', 2],['B', 'D', 5], ['C', 'D', 1]]
#
#P = FW(A, B, C)
# print(P)
