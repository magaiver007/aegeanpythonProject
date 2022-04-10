import numpy as np

while 1:
    try:
        grade: int = int(input("Δώστε τον βαθμό του μαθητή \n"))
        break
    except ValueError:
        print("Παρακαλώ δώστε αριθμό για τον βαθμό του μαθητή \n")
        continue

if grade >= 50:
    print("passing grade")
if grade <= 100 & grade >= 85:
    print("Grade A")
else:
    print("Grade B")

if grade <= 100 and grade >= 85:
    print("Excellent")
elif grade < 85 and grade >= 65:
    print("Very Good")
elif grade < 65 and grade > 50:
    print("Good")
elif grade == 50:
    print("Passing")
else:
    print("Fail")
