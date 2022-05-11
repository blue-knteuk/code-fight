N = int(input())

coin = 0

if N % 100 != 0:
    print(-1)
else:
    coin += N // 500
    coin += (N % 500) // 100
    print(coin)