students = [(50, "Alan"), (25, "Shannon"), (75, "Ada")]


def sort_by_mark(students):
    students_mark = sorted(students, reverse=True)
    return(students_mark)

    


def sort_by_name(students):
    students_name = sorted(students, key=lambda name: name[1])
    return(students_name)


mark = sort_by_mark(students)
names = sort_by_name(students)


print(mark)
print(names)