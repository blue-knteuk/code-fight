S = list(input())
#print(S)

typ = {"a":1, "s":2, "d":3, "f":4, "g":5, "h":6, "j":7, "k":8, "l":9} #辞書作っておく

A = []
for i in range(len(S)): #配列の長さ分rangeで回す
    #print(i) 0 1 2 3
    A.append(typ[S[i]])
    #print(S)
    #print(A)

ans = 0
for i in range(len(S) - 1):
    ans += (abs(A[i] - A[i+1]) + 1) #移動 + クリック1秒

ans = ans + A[0] #全部Aから動くから、A分を足す
print(ans)
