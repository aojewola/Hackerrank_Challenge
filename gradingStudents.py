# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:17:27 2020

@author: DELL
"""

import os

def gradingStudents(grades):
    # Write your code here
    new_grades = list()
    for i in range(len(grades)):
        if grades[i] < 38:
            new_grades.append(grades[i])
        else:
             next_multiple_of_5 = (grades[i] // 5 + 1) * 5
             reminder = next_multiple_of_5 - grades[i]
             if reminder < 3:
                new_grades.append(next_multiple_of_5)
             else:
                new_grades.append(grades[i])
    return new_grades
                
             

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.abspath(__name__), "OUTPUT_PATH"), exist_ok=True)
    fptr = open('OUTPUT_PATH', 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    print(grades)
    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str,result)))
    fptr.write('\n')

    fptr.close()
