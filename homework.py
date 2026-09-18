#1.Getting the input from user
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height in meters: "))
print(name)
print(age)
print(height)
#8.power calculation
base=int(input("Enter the base: "))
exponent=int(input("Enter the exponent: "))
result=base**exponent
print("Result:",result)
#9.average of three numbers
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
average=(n1+n2+n3)/3
print("Average:",average)
#10.greater the comparison
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a>b)
#11.equality check
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print(n1==n2)
#2.personalised greetings
print("hello,jyothika")
#3.add two numbers read as a string
a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=a+b
print("sum of two numbers:",sum)
#4.change float into integer
num=float(input("enter a float number:"))
new=int(num)
print("integer value:",new)
#5.sum using arthematic operators
a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=a+b
print("sum of two numbers:",sum)
#6.area of rectangle
length=float(input("enter the length of rectangle:"))
width=float(input("enter the width of rectangle:"))
area=length*width
print("area of rectangle:",area)
#7.qotient and remainder
a=int(input("enter first number:"))
b=int(input("enter second number:"))
quotient=a//b
remainder=a%b
print("quotient:",quotient)
print("remainder:",remainder)
#12.both positive numbers check
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(a>0 and b>0)
#13.atleast one even number
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
print(n1%2==0 or n2%2==0)
#14.logical not a condition
n=int(input("enter a number:"))
print(not (n%2==0 ))
#15.argument of arthematic operators
a=int(input("enter first number:"))
a+=int(input("enter second number:"))
print("sum:",a)
a*=int(input("enter third number:"))
print("multiplication:",a)
a%=int(input("enter fourth number:"))
print("remainder:",a)
#16.exchange values of two variables
a=int(input("enter first number:"))
b=int(input("enter second number:"))
temp=a
a=b
b=temp
print("After exchanging values:")
print("a:",a)
print("b:",b)
#17.calculate simple intrest
p=float(input("enter principal amount:"))
r=float(input("enter rate of interest:"))
t=float(input("enter time in years:"))
simple_interest=(p*r*t)/100
print("Simple Interest:",simple_interest)
#18.temperature conversion
celsius=float(input("enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in Fahrenheit:",fahrenheit)
#19.check divisibility by 3 and 5
n=int(input("enter a number:")) 
print(n%3==0 and n%5==0)
#20.sum of digits of two digit number
number=int(input("enter number"))
tens=number//10
units=number%10
total=tens+units
print(total)