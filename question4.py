#Python program to evalute student performance based on the conditions below

def students_grades(student_mark):
    
    if student_mark >= 90:
        return "Excellent Performance"
    
    elif student_mark >= 80:
        return "Very Good Performance"
    
    elif student_mark >= 70:
        return "Good Performance"
    
    elif student_mark >= 60:
        return "Average Performance"
    else : return "Poor Perfomance"
    
print(students_grades(60))   
  