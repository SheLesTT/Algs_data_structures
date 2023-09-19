n, programs = map(int, input().split())
places = list(map(int, input().split()))

students =[]
for _ in range(n):
    students.append(list(map(int, input().split())))

enters= [0]*n
for idx, student in enumerate(students):
    student.append(idx)
sort_st = sorted(students, key=lambda x: x[0])
for student in sort_st:
    entered = False
    for program in student[2:-1]:

        if places[program-1] > 0:
            places[program-1] -= 1
            enters[student[-1]] = program
            entered = True
            break
    if not entered:
        enters[student[-1]] = -1

print(*enters)