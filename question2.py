# Creating the classroom model
class Classroom:
    #Defining the model attributes
    def __init__(self, classroom_number, teacher,student_name,student_age,):
        self.classroom_number = classroom_number
        self.teacher = teacher
        self.student_name = student_name,
        self.student_age = student_age,
        # self.student_school = student_school,
         
# Function to  add a new student   
    def add(self, classroom_number, teacher,student_name,student_age ):
        new_student = Classroom(classroom_number, teacher,student_name,student_age )
        new_student_list.append( new_student)
  
# Function to display Classroom details     
    def show_details(self, ob):
            print("Classroom_number  : ", ob.classroom_number)
            print("Student_name : ", ob.student_name)
            print("Student_age : ", ob.student_age)
            print("Teacher's name : ", ob.teacher)
            print("\n")    
         
#Querying the student by name 
    def query_student(self,student_name):
        for m in range(new_student_list.__len__()):
            if(new_student_list[m].student_name == student_name):
                return m       
  
# Delete Function                                  
    def delete(self, student_name):
        n = new.query_student(student_name)  
        del new_student_list[n]
  
   # Delete Function                                  
    def age(self, specific_age):
        for i in range(new_student_list.__len__()):
            if(new_student_list[i].student_age == specific_age):
                return i 
   
    # Update List   
    def update(self, student_name, New):
        m = new.query_student(student_name)
        updated = New
        new_student_list[m].student_name = updated;
        
# list to add a student to the classroom
new_student_list =[]
# Creating an object for the classroom model,
new = Classroom('Q001', "Madam Janet", "Nabatanzi Gorret", 21)
  

  
# new students
new.add('Q001', "Madam Janet", "Nabatanzi Gorret", 21)
new.add('Q002', "Madam Judith", "Mbabazi Joy", 20)
new.add('Q003', "Madam Grace", "Aladina DAP", 20)


print("\nStudents details\n")
for i in range(new_student_list.__len__()):    
    new.show_details(new_student_list[i])
             

l = new.age(21)
new.show_details(new_student_list[l])
         

new.delete("Mbabazi Joy")
print(new_student_list.__len__())
print("New classroom list after deleting a specific student")
for i in range(new_student_list.__len__()):    
    new.show_details(new_student_list[i])
             

             

    