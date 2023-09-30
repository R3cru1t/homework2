n = int(input())
pupils = {}
MARKS_COUNT = 3
marks = [0 for s in range(MARKS_COUNT)]
for i in range(n):
    pupil = input().split()
    pupils[pupil[0]] = [int(i) for i in pupil[1:]]
    for i in range(MARKS_COUNT):
        marks[i] += pupils[pupil[0]][i]
    for i in range(MARKS_COUNT):
        print(marks[i]/n)