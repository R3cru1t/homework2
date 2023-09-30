n = int(input())
pupils = []
MARKS_COUNT = 3
for i in range(n):
    pupil = input().split()
    pupil[1:] = [int(i) for i in pupil[1::]]
    pupil.insert(0, -sum(pupil[1:]) / MARKS_COUNT)
    pupils.append(pupil)
pupils.sort()
for h in pupils:
    print('%s %s %.2f' % (h[1],
                        ' '.join([str(mark) for mark in h[2:]]),
                        -h[0]))