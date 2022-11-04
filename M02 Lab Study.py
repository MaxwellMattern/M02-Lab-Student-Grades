#   Maxwell Mattern
#   M02 Lab: Student Grades
#   App accepts a student name and GPA and displays whether the student qualifies for
#   Deans list or Honor Roll.

# Request user input for student last name.
studentLast = input('Please input students last name or "ZZZ" to quit: ')

# While student last name is not ZZZ, run loop.
while studentLast != "ZZZ":
    
    # Request student first name and GPA.
    studentFirst = input('Please input students first name: ')
    studentGpa = float(input('Please input student GPA: '))
    
    # If student GPA greater than 3.5 display answer and prompt user for the next students last name.
    if studentGpa >= 3.5:
        print('This student has made Deans List!')
        studentLast = input('Please input the next students last name or "ZZZ" to quit: ')
    
    # If student GPA greater than 3.25 display answer and prompt user for the next students last name.
    elif studentGpa >= 3.25:
        print('This student has made the Honor Roll!')
        studentLast = input('Please input the next students last name or "ZZZ" to quit: ')
    
    # If student GPA less than 3.25 display answer and prompt user for the next students last name.
    else:
        studentLast = input('This student does not qualify for Deans List or Honor Roll. Please input the next students last name or "ZZZ" to quit: ')

# If user inputs ZZZ for student last name, exit loop and end program.
else:
    print('Good Bye')
