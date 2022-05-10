S = list(input())
N = int(input())

for i in range(N):
    S.insert(0, "a") #リストの特定の位置に要素を追加する
print("".join(S))