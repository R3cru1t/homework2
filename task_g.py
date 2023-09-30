N = int(input())
P = [int(s) for s in input().split()]
M = int(input())
Q = [int(s) for s in input().split()]
lenght_R = max(N, M) + 1
R = [0] * lenght_R
for i in range(lenght_R):
    R[i] = (P[i] if i <= N else 0) + (Q[i] if i <= M else 0)
while lenght_R > 0 and R[lenght_R - 1] == 0:
    lenght_R -= 1
if lenght_R == 0:
    print(0)
else:
    print(*R[:lenght_R])
