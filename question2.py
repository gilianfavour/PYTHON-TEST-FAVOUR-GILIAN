# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

import math
def student_mark ():
    #Prompting the student to enter marks

    
    percentage = float(input('Enter your mark scored: \n'))
    
    if percentage >= 90:
        return('Grade A')

    elif percentage >= 80:
        return('Grade B')

    elif percentage >= 70:
        return('Grade C') 
 
    elif percentage >= 60:
        return('Grade D')

    elif percentage >= 40:
        return ('Grade E')

    else:return ('Grade F')
    
    
student_mark () 