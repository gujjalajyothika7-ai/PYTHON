name,age,marks="ravi",20,85
print(name)
print(age)
print(marks)
a,b,c=10,20,30
print(a)
print(b)
print(c)
x="python"
x="malla reddy"
print(x)
a=b=c=10
print(a)
print(b)
print(c)
productname="santoorsoap"
price=60.25
pincode=500090
location="hyderabad"
print(productname)
print(price)
print(pincode)
print(location)
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
#SLICING
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
print(numbers[1:7:2])
print(numbers[6:1:-2])
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
#arthematic operators
a=10
b=40
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("modulus:",a%b)
print("power:",a**b)
#simple calculator
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("modulus:",a%b)
print("power:",a**b)
#student marks calculator
marks1=int(input("Enter your first subject marks:"))
marks2=int(input("Enter your second subject marks:"))
marks3=int(input("Enter your third subject marks:"))
total=marks1+marks2+marks3
average=total/3
print("Total marks:",total)
print("Average marks:",average)
#shopping bill calculator
price1=float(input("Enter product 1 price:"))
price2=float(input("Enter product 2 price:"))
price3=float(input("Enter product 3 price:"))
price4=float(input("Enter product 4 price:"))
TOTAL=price1+price2+price3+price4
discount=TOTAL*0.10
final_amount=TOTAL-discount
print("Total amount:",TOTAL)
print("Discount amount:",discount)
print("Final amount to be paid:",final_amount)
#salary calculator
basic=float(input("Enter basic salary:"))
hra=basic*0.20
da=basic*0.10
gross_salary=basic+hra+da
print("BASIC SALARY:",basic)
print("HRA:",hra)
print("DA",da)
print("GROSS SALARY:",gross_salary)
#time calculator
a=int(input("Enter minutes:"))
print("Seconds:",a*60)
print("Hours:",a/60)
print("Remaining minutes:",a%60)
#assignment operators
x=10
x+=5
print(x)
x-=2
print(x)
x*=3
print(x)
x/=2
print(x)
x//=4
print(x)
x%=2
print(x)
#bank balance
balance=1000
deposit=500
balance+=deposit
print("AFTER DEPOSIT:",balance)
withdraw=200
balance-=withdraw
print("AFTER WITHDRAWAL:",balance)
#bitwise operators
a=13
b=5
print(a&b)
print(a|b)
print(a^b) #xor means not
print(a<<b)
print(a>>b)
#electriity bill calculator
units=int(input("Enter electricity units:"))
rate=6
bill=units*rate
print("Electricity bill:",bill)
#travel expen calulator
travel=float(input("Travel expence:"))
food=float(input("Food expence:"))
hotel=float(input("Hotel expence:"))
total=travel+food+hotel
print("Total expence:",total)
#comparision operators
a=10
b=20
print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>b:",a>b)
print("a<b:",a<b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)
#age elgibility checker
age=int(input("enter your age:"))
print("Eligible:",age>=18)
#pass or fail checker
marks=int(input("enter your marks:"))
print("passed:",marks>=40)
#login vadilation
corret_username="admin"
correct_password="admin123"
username=input("Enter your username:")
password=input("Enter your password:")
print(username==corret_username)
print(password==correct_password)
#Logical operators
age=25
citizen=True
print(age>=18 and citizen==True)
age=16
citizen=True
print(age>=18 and citizen==True)
a=False
b=True
print(a or b)
a=True
print(not a)
#atm elgibility checker
balance=10000
withdraw=5000
print("Eligible for withdrawal:",balance>=withdraw)
#student scholorship eligibility checker
marks =float(input("Enter your marks:"))
attendence=float(input("Enter your attendance:"))
eligible =marks>=85 and attendence>=75
print("Sholorship elgible:",eligible)
#identity operator
a=None
print(a is None)
print(a is not None)
#if
age=int(input("Enter your age:"))
if age>=18:
   print("Eligible")
#if else
#1
age=18
if age>=20:
   print("Eligible")
else:
     print("Not eligible")
#2
marks=40
if marks>=35:
   print("pass")
else:
    print("fail")
#if elif else
marks=int(input("Enter your marks:"))
if marks>=90:
   print("A grade")
elif marks>=80:
   print("B grade")
elif marks>=70:
   print("C grade")
else:
   print("D grade")
#nested if else
   age=int(input("Enter your age:"))
   if age>=18:
      print("Eligible")
   else:
      print("Not eligible")
#pass or fail
marks=int(input("Enter your marks:"))      
if marks>=35:
   print("pass")
else:
   print("fail")
#positive or negative
num=int(input("Enter a number:"))
if num>0:
   print("Positive number")
else:
   print("Negative number")
#greater than number
num=int(input("Enter first number:"))
if num>100:
   print("Greater than 100")
else:
   print("Not greater than 100")

a=int(input("Enter first number:"))   
b=int(input("Enter second number:"))
if a>b:
   print("largest:",a)
elif b>a:
   print("largest:",b)   
else:
   print("largest:",a)

num=int(input("Enter a number:"))
if num>0:
   print("Positive number")
elif num<0:
   print("Negative number")
else:
   print("Zero")
   #operations
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
operator=input("Enter operator(+,-,*,/):")
if operator=="+":
   print("result:",a+b)
elif operator=="-":
   print("result:",a-b)
elif operator=="*":
   print("result:",a*b)
elif operator=="/":
   print("result:",a/b)
else:
   print("Invalid operator")
   #marks and attendence
marks=int(input("Enter your marks:"))
attendence=int(input("Enter your attendence:"))
if marks>=35 and attendence>=75:
   print("Eligible for next class")
else:
   print("Not eligible for next class")
   #username and password
username=input("Enter your username:")
password=input("Enter your password:")
if username=="admin" and password=="1234":
   print("Login successful")
else:
   print("Login failed")
#bank withdrawl
balance=float(input("Enter your balance:"))
amount=float(input("Enter amount to withdraw:"))
if amount>0:
   if amount<=balance:
     balance = balance-amount
     print("Withdrawal successful")
   else:
     print("Insufficient balance")
else:
    print("Invalid amount")
#license eligibility
age=int(input("Enter your age:"))
test=input("Have you passed the driving test? (yes/no):")
if age>=18 and test.lower()=="yes":
   print("Eligible for license")
   if test=="yes":
      print("You have passed the driving test")
   else:
      print("You have not passed the driving test")
else:
   print("Not eligible for license")
#print all prime numbers between 2 to 100
for num in range(2, 101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
            if count==2:
               print(num)
#break statement
for i in range(1,11):
    if i==5:
        break
    print(i)
#continue statements
for i in range(1,11):
    if i==5:
        continue
    print(i)
#pass keyword
for i in range(1,11):
    if i==5:
        pass
    print(i)
#Elgibile not eligible
age=int(input("Enter your age:"))
if age>=18:
   print("Eligible")
   print("You are eligible to vote")
else:
   print("Not eligible")
   print("You are not eligible to vote")
#print all odd numbers from 1to 50 by using continuity 
for i in range(1,51):
    if i%2!=0:
        continue
print(i)
#print numbers until user enters 0
while True:
   number = int(input("Enter number:"))
   if number==0:
      break
if number>0:
   print("Positive number")
#print number from 1 to 100,but skip multiples of 3 and stops at 50
for i in range(1,101):
    if i%3==0:
        continue
    if i>50:
       break
    print(i)
#calculate sum of positive numbers entered by user 
total=0
while True:
  number=int(input("Enter a number:"))
  if number<0:
      continue
      if number==0:
        break
  total=total+number
  print("Sum of positive numbers:",total)
  #find the first number between 1 to 100 that is divisible by 3 and 5
for i in range(1,101):
      if i%3==0 and i%5==0:
         print("First number divisible by 3 and 5:",i)
         break
#calculate the sum of positive numbers entered by user 
total=0
for i in range(10):
  number=int(input("enter number:"))
  if number<0:
        continue
total=total+number
print("Sum of positive numbers:",total)
#check with limited attempts
corret_password="python123"
for attempt in range(1,4):
    password=input("Enter your password:")
    if password==corret_password:
        print("Login successful")
        break
    print("wrong password")
else:
      print("acount is locked")
#find the largest number among 5 numbers entered by user
largest=None
for i in range(5):
      number=int(input("Enter a number:"))
      if largest is None or number>largest:
         largest=number
print("Largest number:",largest)
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
#check prime numbers
number=int(input("enter number:"))
count=0
for i in range(1,number+1):
    if number%i==0:
         count=count+1
if count==2:
     print("the number is prime")
else:
     print("the number is not prime")
#loop names     
     name=input("enter your name:")
     for name in name:
         print(name)