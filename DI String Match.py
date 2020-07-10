def diStringMatch(S):
    A=[i for i in range(len(S)+1)]
    lo = 0
    hi = len(S)
    for j in range(len(S)):
        if S[j]=='I':
            A[j]=lo
            lo+=1
        else:
            A[j]=hi
            hi-=1
    A[len(S)] = lo
    return A
print(diStringMatch("IDID"))