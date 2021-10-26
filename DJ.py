def DJ(u , z, A, B, C):
    L = []
    S = []
    for i in range(len(A)):
        L.append(float("inf"))
    
    o = A.index(u)
    p = A.index(z)

    L[o] = 0 
    
    while z not in S:
        print(S)
        x = 0
        for i in range(len(A)):
            if A[i] not in S: 
                if L[i] < L[x]:
                    x = i
        
        S.append(A[x])
        for i in range(len(A)):
            if A[i] not in S:
                if (A[x], A[i]) in C:
                    m = C.index((A[x], A[i]))
                    L[i] = min(L[i], L[x] + (B[m])[2])

                elif (A[i], A[x]) in C:
                    m = C.index((A[i], A[x]))
                    L[i] = min(L[i], L[x] + (B[m])[2])
    
    return S, L[p]

A = ['A', 'B', 'C', 'D']
C = [('A', 'B'), ('A', 'C'), ('A', 'D'),('B', 'D'), ('C', 'D')]
B = [('A', 'B', 3), ('A', 'C', 4), ('A', 'D', 2), ('B', 'D', 5), ('C', 'D', 1)]

P, p = DJ('C', 'B', A, B, C)
print(P)
print()
print(p)