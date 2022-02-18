#nested dictionary called classroom

classroom = {
    1: {'name':"Nabatanzi Gorret",
        'age':21,
        'school':"Buddo SS"
     },
    
    2: {'name':"Mbabazi Joy",
     'age':20,
     'school':"Gayaza SS"
     },
    
     3: {'name':"Arah  Robinah",
     'age':22,
     'school':"St Julian Girls SS"
     },
     
      4: {'name':"Aladina Faith",
     'age':23,
     'school':"Lubiri SS"
     }
}


#looping through the dictionary
for classroom_id, classroom_info in classroom.items():
    print("\nStudent ID:", classroom_id)
    
    for y in classroom_info:
        print(y + ':', classroom_info[y])

