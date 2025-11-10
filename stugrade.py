import sys


if len(sys.argv) != 6:
    print("Please provide marks of 5 subjects as command line arguments.")
    sys.exit()


marks = [int(arg) for arg in sys.argv[1:6]]


average = sum(marks) / len(marks)


if average >= 90:
    grade = "A"
else:
    if average >= 75:
        grade = "B"
    else:
        if average >= 60:
            grade = "C"
        else:
            if average >= 40:
                grade = "D"
            else:
                grade = "Fail"

# Print results
print("Average Marks:", round(average, 2))
print("Grade:", grade)