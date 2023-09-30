N = int(input())
P = [int(s) for s in input().split()]
M = int(input())
Q = [int(s) for s in input().split()]
print(*sorted(P + Q))