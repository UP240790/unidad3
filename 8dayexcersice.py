#1
dog = {}
 
 #2
dog = {'name':'princesa',
        'color':'blaco',
        'breed':'petit',
        'legs':4,
        'age':9}
 
 #3
student = {
     'first_name':'dante',
     'last_name':'Gonzalez',
     'gender':'hombre',
     'age':18,
     'marital_status':'relationship',
     'skills':['Python','SQL','HTML','CSS','JS'],
     'country':'England',
     'city':'CDMX',
     'addres':{
         'street':'madrid 451',
         'zipcode':'20235',
     }
 }
 
 #4
print(f'The lenght of the student dictionary is {len(student)}')
 
 #5
print(f'The data type of student skills is {type(student["skills"])}')
 
 #6
student['skills'].append('PHP')
print(student['skills'])
 
 #7
keyList = list(student.keys())
print(keyList)
 
 #8
valList = list(student.values())
print(valList)
 
 #9
studentTuple = student.items()
print(studentTuple)
 
 #10
student.pop('gender')
print(student)
 
 #11
del dog