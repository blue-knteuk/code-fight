N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
#print(N, A, B)

for i in range(N):
    #print(i) 0 1 2 3
    if A[i] < B[i]:
        break
print(i+1)