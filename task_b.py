N = int(input())
a = [int(s) for s in input().split()]
p = int(input())
a.insert(0, a.pop(p-1))
print(' '.join([str(x) for x in a]))