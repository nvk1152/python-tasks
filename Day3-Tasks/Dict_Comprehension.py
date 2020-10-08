# Using Dict Comprehension to print students with 'cse' department

# Student details
students = [
    ("Vamsi", "CSE"),
    ("Raju", "ECE"),
    ("Mike", "EEE"),
    ("Sam", "CSE"),
    ("Bob", "CSE")
]

# Mapping student details to name using dictionary
student_dep = {user[0] : user[1] for user in students}

for name, det in student_dep.items():
    if "CSE" in det :
        print(name)