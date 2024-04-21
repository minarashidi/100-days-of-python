import random
import pandas

# Dictionary Comprehension
# Creating a new dictionary from an existing list
# new_dict = {new_key:new_value for item in list}

# Generating random score for each student
students = ["John", "Smith", "Mina", "William", "Nick", "Sara"]
students_score = {student: random.randint(1, 100) for student in students}
print(students_score)

# Creating a new dictionary from an existing dictionary
# new_dict ={new_key:new_value for (key,value) in dict.items() }
passed_student = {student: score for student, score in students_score.items() if score >= 60}
print(passed_student)

# Loop through a data frame
students_dict = {"students": ["mina", "sara", "william"],
                 "scores": ["B", "A", "c"]}
students_df = pandas.DataFrame(students_dict)
print(students_df)

# Loop through rows of a data frame
for (index, row) in students_df.iterrows():
    print(row.students, row.scores)
