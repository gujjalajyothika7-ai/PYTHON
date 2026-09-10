#integers
a=10
print(a)
print(type(a))
b=20
print(b)
print(type(b))
#boolean
a=True
print(a)
print(type(a))
#float
x=3.14
print(x)
print(type(x))
#string
name="jyothika"
print(name)
print(type(name))
#list
numbers=[1,2,3,4,5]
print(numbers)
print(type(numbers))
#tuple
coordinates=(10,20)
print(coordinates)
print(type(coordinates))
#set
unique_numbers={1,2,3,4,5}
print(unique_numbers)
print(type(unique_numbers))
#dictionary
student={"name":"jyothika","age":17,"branch":"cse"}
print(student)
print(type(student))
#list in python
#list is an order and changeable collection that can store a sequence of items
marks=[80,90,86,70,75]
print(marks)
#accessing elements in a list
marks=[80,90,86,70,75]
print(marks[0])
print(marks[2])
print(marks[4])
print(marks[3])
print(marks[1])
#change elements in a list
marks=[80,90,86,70,75]
marks[0]=85
#add elements in a list
marks=[85,90,86,70,75]
marks.append(80) #add the element at the last position
print(marks)
#remove the elements from the list
marks=[85,90,86,70,75,80]
marks.remove(70)  
print(marks)
# insert the elements in the list
marks=[85,90,86,75,80]
marks.insert(3,70) 
marks.insert(0,95)
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)
#clear the list
marks=[95,85,90,86,75,80]
marks.clear()
print (marks)
#index of list
marks=[95,85,90,86,75,80]
print(marks.index(90))
print(marks.index(75))
print(marks.index(80))
#count of list
marks=[95,85,90,86,75,80,90,86]
print(marks.count(90))
print(marks.count(75))
#sorting the list
marks=[95,85,90,86,75,80,90,86]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
#reverse
marks=[90,95,97,88]
marks.reverse()
print (marks)
#copy
marks=[90,95,97,88]
b=marks.copy()
print(b)
#start stop step
numbers=[10,20,30,40,50,60,70,80,90,100]
print(numbers[2:8])
print(numbers[2:8:2])
print(numbers[::2])
print(numbers[1::2])
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
#tuples in python
#tuple is a collection of multiple values that is ordered and unchangeable
student=("Jyothika",17,"CSE")
print(student[0])
#access elements in a tuple
student=("Jyothika",17,"CSE")
print(student[0])
print(student[1])
print(student[2])
#immutable nature of tuple
#this gives an error because tuple is immutable
numbers=(10,20,30,40,50)
print(numbers.count(20))
#index
print(numbers.index(30))
#max,min,sum,length
numbers=(10,20,30,40,)
print(len(numbers)) #4
print(max(numbers)) #40
print(min(numbers)) #10
print(sum(numbers)) #100
#sets in python
#sets are unordered and unindexed collection of unique elements that is ordered and mutable
numbers={10,20,30,20,10}
print(numbers)
#why use sets
#1. To remove duplicates from a list
#2. To perform mathematical operations like union, intersection, difference
#3. To check if an element is present in the set
subjects={"Maths","Science","English","Social","Maths","English"}
print(subjects)
#add values to a set 
subjects.add("Hindi")
print(subjects)
#remove the values from a set
subjects.remove("Social")
print(subjects)
#sets do not allow duplicate values
numbers={1,2,3,3,2,5}
print(numbers) 