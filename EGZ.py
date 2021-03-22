def EGZ_prime(p, a):
    k = sorted(range(2*p-1), key=lambda x: a[x]%p)
    L = [False] * (2*p-1)
    for i in range(p-1):
        if a[k[1+i]]%p == a[k[p+i]]%p:
            for i in range(1+i, 1+p+i):
                L[k[i]] = True
            return L

    s = sum((a[k[i]] for i in range(p))) % p
    T, D = [False]*p, [None]*p
    T[s] = True
    for i in range(p-1):
        if T[0]: break
        d = (a[k[p+i]]-a[k[1+i]])%p
        l, h = s*pow(d, -1, p)%p, p
        while l+1 != h:
            m = (l+h)//2
            if T[m*d%p]: l = m
            else: h = m
        T[h*d%p], D[h*d%p] = True, i

    c = 0
    for i in range(p): L[k[i]] = True
    while s != c:
        L[k[p+D[c]]], L[k[1+D[c]]] = True, False
        c = (c - (a[k[p+D[c]]]-a[k[1+D[c]]]))%p

    return L

def EGZ_composite(p, q, a):
    S, T = list(range(p-1)), [None]*(2*q-1)
    for i in range(2*q-1):
        S.extend(range((i+1)*p-1, (i+2)*p-1))
        ret = EGZ(p, [a[s] for s in S])
        T[i] = [S[j] for j in range(2*p-1) if ret[j]]
        S = [S[j] for j in range(2*p-1) if not ret[j]]
    L = [False]*(2*p*q-1)
    ret = EGZ(q, [sum(a[t] for t in T[i])//p for i in range(2*q-1)])

    for i in range(2*q-1):
        if ret[i]:
            for j in T[i]: L[j] = True

    return L

def EGZ(n, a):
    if n == 1: return [True]
    for i in range(2, n):
        if n%i == 0: return EGZ_composite(i, n//i, a)
    return EGZ_prime(n, a)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ret = EGZ(N, A)
    print(' '.join(map(str, [A[i] for i in range(2*N-1) if ret[i]])))
