N = int(input())
A = list(map(int, input().split()))
#print(N, A)

#左から踏破
left = 0
for i in range(N-1):
    #print(i)
    left += (max(0, A[i+1] - A[i]))
    #print(f"{i}番目 {left}")
#print(left)

#右から踏破
right = 0
for i in reversed(range(N-1)):
    #print(i)
    right += (max(0, A[i] - A[i+1]))
#print(right)

print(min(left, right))