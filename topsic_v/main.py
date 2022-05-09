N = int(input())
S = list(input())
#print(N, S)

box = 1 #1箱は絶対必要だから初期値は1にしておく

for i in range(N-1):
    if S[i] != S[i+1]:
        box += 1
print(box)