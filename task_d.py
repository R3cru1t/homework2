n = int(input())
pupils = {}
MARKS_COUNT = 3
for i in range(n):
    pupil = input().split()
    pupils[pupil[0]] = [int(i) for i in pupil[1:]]
    print('%s %.2f' % (pupil[0],
          sum(pupils[pupil[0]]) / MARKS_COUNT))