#   Maxwell Mattern
#   M02 Lab: Student Grades
#   App accepts a student name and GPA and displays whether the student qualifies for
#   Deans list or Honor Roll.

studentLast = input('Please input students last name or "ZZZ" to quit: ')

while studentLast != "ZZZ":
    studentFirst = input('Please input students first name: ')
    studentGpa = float(input('Please input student GPA: '))
    if studentGpa > 3.5:
        print('This student has made Deans List!')
        studentLast = input('Please input the next students last name or "ZZZ" to quit: ')
    elif studentGpa > 3.25:
        print('This student has made the Honor Roll!')
        studentLast = input('Please input the next students last name or "ZZZ" to quit: ')
    else:
        studentLast = input('This student does not qualify for Deans List or Honor Roll. Please input the next students last name or "ZZZ" to quit: ')

else:
    print('Good Bye')
