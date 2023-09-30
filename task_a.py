N = int(input())
a = [int(s) for s in input().split()]
p = int(input())
print(' '.join(str(i) for i in a if i != p))