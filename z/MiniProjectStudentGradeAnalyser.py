
# 1) Students Data

students=[
    ("Alice",95),
    ("Bob",67),
    ("charlie",82),
    ("David",38),
    ("Eva",74),
    ("Farhan",59),
]

# 2) Assign grades using list comprehensions

graded_students=[
    (
        name,marks,
        'A' if marks>=90 else
        'B' if marks>=75 else
        'C' if marks>=60 else
        'D' if marks>=45 else
        'F'
    )
    for name,marks in students
]

print(graded_students)

for student in graded_students:
    print("Name:",student[0],",Marks:",student[1],",Grade:",student[2])