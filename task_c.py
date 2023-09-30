N = int(input())
a = [int(s) for s in input().split()]
p = int(input())
a.pop(p-1)
(q, k) = [int(o) for o in input().split()]
a.insert(q-1, k)
print(' '.join([str(x) for x in a]))