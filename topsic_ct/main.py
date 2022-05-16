N = int(input())
A = [int(input()) for x in range(N)]
#print(N, A)

X, Y = 0, 0

for i in range(1, N+1):
    #print(i)
    if i % 4 == 0:
        Y = Y + A[i-1]
    elif i % 4 == 3:
        X = X - A[i-1]
    elif i % 4 == 2:
        Y = Y - A[i-1]
    else:
        X = X + A[i-1]
print(X, Y)
