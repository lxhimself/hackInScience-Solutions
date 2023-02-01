

students = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]
threshold = 25



def select_student(students, threshold):
    accepted = []
    refused = []
    selection = {}
    for i in students:
        if i[1] >= threshold:
            accepted.append(i)
        else:
            refused.append(i)

    accepted.sort(key= lambda x: x[1], reverse = True)
    refused.sort(key= lambda x: x[1])
    selection.update({"Accepted": accepted})
    selection.update({"Refused": refused})
    return(selection)


print(select_student(students, threshold))