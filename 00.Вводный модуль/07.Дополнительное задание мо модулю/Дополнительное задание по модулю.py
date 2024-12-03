grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
    ]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(list(students))
union_data ={students[i]: (sum(grades[i]) / len(grades[i])) for i in range(len(grades))}
print(union_data)
