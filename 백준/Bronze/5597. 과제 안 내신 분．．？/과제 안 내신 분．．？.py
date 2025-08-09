submit_student = []

for _ in range(28):
    student = int(input())
    submit_student.append(student)

all_student = set(range(1,31))

not_submit_student = sorted(all_student - set(submit_student))

for s in not_submit_student:
    print(s)