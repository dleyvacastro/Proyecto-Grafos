import numpy as np
def FW(A, B, C):
    z = len(A)
    W = np.zeros((z, z))

    for i in range(z):
        for j in range(z):
            if [A[i], A[j]] in C:
                m = C.index([A[i], A[j]])
                (W[i])[j] = (B[m])[2]
                (W[j])[i] = (B[m])[2]
            elif [A[j], A[i]] in C:
                m = C.index([A[j], A[i]])
                (W[i])[j] = (B[m])[2]
                (W[j])[i] = (B[m])[2]
    L = np.zeros((z, z))
    for i in range(z):
        for j in range(z):
            if (W[i])[j] != 0:
                (L[i])[j] = (W[i])[j]
                (L[j])[i] = (W[i])[j]
            if i != j and (W[i])[j] == 0:
                (L[i])[j] = 20
                (L[j])[i] = 20
    
    L1 = np.zeros((z, z))
    for n in range(z):
        for i in range(z):
            for j in range(z):
                (L1[i])[j] = min((L[i])[j], (L[n])[j] + (L[i])[n])
                (L1[j])[i] = min((L[i])[j], (L[n])[j] + (L[i])[n])
        
        L = L1
        L1 = np.zeros((z, z))
    
    return L


A = ['A', 'B', 'C', 'D']
C = [['A', 'B'], ['A', 'C'], ['A', 'D'],['B', 'D'], ['C', 'D']]
B = [['A', 'B', 3], ['A', 'C', 4], ['A', 'D', 2],['B', 'D', 5], ['C', 'D', 1]]

P = FW(A, B, C)
print(P)