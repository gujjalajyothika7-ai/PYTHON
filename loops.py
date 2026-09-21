#use "for"when you know how many times you want to loop through a block of code
#looping through numbers 1 to 5
for i in range (1,6):
   print(i)
#using "while"when repetition depends on a condition 
# looping through numbers 1to 5
i=1
while i<=5:
   i=i+1
   print(i)
#print numbers from 1 to 10
for i in range (1,11):
   print(i)
# print numbers from 10 to 1
for i in range(10,0,-1):
   print(i)
#print even numbers from 1 to 50
for i in range (0,51,2):
   print(i)
#print odd numbers from 1 to 50
for i in range (1,51,2):
   print(i)
#print multiple of 5 from 1 to 50
for i in range(5,51,5):
   print(i)
#multiplication table 
number=int(input("enter number:"))
for i in range(1,11):
   print(number,"x",i,"=",number*i)
#sum of numbers from 1to n
n=int(input("enter number:"))
total=0
for i in range (1,n+1):
   total=total+1
#factorial of a number
n= int(input("enter number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("factorial:",factorial)
#sum o even numbers from 2 to n
n=int(input("enter number:"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
    print("sum of even numbers:",sum)
#count of multiples of 3
n=int(input("enter number:"))
count=0
for i in range(1,n+1):
    if i%3==0:
        count=count+1
print("count of multiples of 3:",count)
#sum of multiples of 5
n=int(input("enter number:"))
total=0
for i in range(1,n+1):
   if i %5==0:
    total=total+i
print("sum of multiples of 5:",total)
#print all even numbers from 2 to 50
i=2
while i<=50:
   print(i)
i=i+2
#print total of no entered by user until user enters 0
total=0
number=int(input("enter number:"))
while number!=0:
    total=total+number
    number=int(input("enter number:"))
    print("total:",total)
#password check
password=""
while password !="python123":
   password=input("enter password:")
   print("login sucessful")