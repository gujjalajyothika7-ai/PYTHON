#key value pair
student={'name':'Joe','age':17,'course':'Python','city':'New York'}
print(student.keys())
print(student.values())
print(student.items())
#access elements in a dictionary
print(student['name']) 
print(student['age']) 
print(student['course']) 
#change elements in a dictionary
student['age'] = 18
print(student['age']) 
#add new data in a dictionary
student['city'] = 'New York'
print(student)
#remove data from a dictionary
student.pop('city')
print(student)
#get() method in a dictionary
print(student.get('name'))
#update() method in a dictionary
student.update({'age':19})
#setdefault() method in a dictionary
student.setdefault('gender','female')
#popitem() method in a dictionary
student.popitem()
print(student)