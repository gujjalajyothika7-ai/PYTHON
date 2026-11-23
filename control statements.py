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
