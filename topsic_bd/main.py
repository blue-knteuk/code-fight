N = int(input())
A = list(map(int, input().split()))

A_list = sorted(A) #昇順に並び替え
#print(A_list)
flag = False

for i in range(N-1):
   if A_list[i] == A_list[i+1]:
       flag = True

if flag == True:
   print("NO")
else:
   print("YES")