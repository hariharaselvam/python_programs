"""
Percentage Calculation of Marks
Python version 2.7.10
Written by Hariharaselvam Balasubramanian
"""
print "Percentage Calculation of Marks"
print "*******************************"

subjects_count = raw_input("Enter the number of subjects       : ")
subjects_count = int(subjects_count)

maximum_marks = raw_input("Enter the maximum mark for each    : ")
maximum_marks = int(maximum_marks)

pass_mark = raw_input("Enter the mark to consider as pass : ")
pass_mark = int(pass_mark)


result = "Pass"
marks = []

for i in range(subjects_count):
    mark = raw_input("Enter the marks of Subject %d       : " % (i + 1))
    marks.append(float(mark))
    if float(mark) < pass_mark:
        result = "Fail"

total_marks = sum(marks)
average_marks = total_marks / subjects_count
percentage = average_marks / maximum_marks * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70 and percentage < 80:
    grade = "B"
elif percentage >= 60 and percentage < 70:
    grade = "C"
elif percentage >= 40 and percentage < 60:
    grade = "D"
else:
    grade = "E"

print ""
print "Total Marks   : ", total_marks
print "Average       : ", average_marks
print "Percentage    : ", str(percentage) + "%"
print "Grade         : ", grade
print "Result        : ", result
print ""
