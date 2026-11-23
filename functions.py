#basic functions
def greet():
    print("hello")
    print("welcome to python programming")
greet()
#functions without parameters
def welcome():
    print("welcome to python programming")
welcome()
welcome()
welcome()
#funtion with parameters
def greet(name):
    print("Hello",name)
greet ("jyothika")
greet("sukeerthi")  
#multiple parameters
def add(a,b):
    print("sum:",a+b)
add(5,10)
add(15,20)
#funtions with return values
def add(a,b):
    return a+b
result=add(5,10)
print(result)
if result>10:
    print("result is greater than 10")
#function for even or odd
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
    return num%2==0
result=even_odd(5)
print(result)
#funtions for largest of two numbers
def largest_of_two(a,b):
    if a>b:
        return a
    else:
        return b
result=largest_of_two(5,10)
print(result)
#function +user input 
def square(number):
    return number*number
number= int(input("Enter number:"))
result=square(number)
print("square:",result)
#sum of two numbers given by the user
def add(a,b):
    return a+b
a=int(input("enter first number:"))
b=int(input("enter second number:"))
result=add(a,b)
print("sum:",result)
#even or odd user input
def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
num=int(input("enter number:"))
result=even_odd(num)
print(result)
#largest of three numbers user input
def largest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
result=largest_of_three(a,b,c)
print(result)
#grade calculation
def find_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return"B"
    elif marks>=70:
        return"C"
    elif marks>=60:
        return"D"
    elif marks>=40:
        return"E"
    else:
        return"F"
marks=int(input("enter marks:"))
result=find_grade(marks)
print("grade:",result)
#functio+loop
def multiplication_table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
        i+=1
    return num*i
num=int(input("enter number:"))
result=multiplication_table(num)
print(result)
#function with sum of 1 to n numbers
def sum_of_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input("enter n:"))
result=sum_of_n(n)
print("sum of 1 to",n,"is:",result)
#positive or negative numbers
def positive_negative(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
num=int(input("enter number:"))
result=positive_negative(num)
print(result)
#factorial of a number
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
n=int(input("enter number:"))
print("factorial=",factorial(n))
#sum of digits of a number
def sum_of_digits(n):
  total=0
  while n>0:
    digit=n%10
    total= total+digit
    n=n//10
    return total
num=int(input("enter number:"))
print("sum of digits:",sum_of_digits(num))
#palindromes
def is_palindrome(s):
    original=n
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    if original==reverse:
        return True
    else:
        return False
num=int(input("enter number:"))
if is_palindrome(num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
#prime numbers check
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input("enter number:"))
if is_prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
#add,sub,multiply,divide
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divided by zero"
    return a/b
x=float(input("enter first number:"))
y=float(input("enter second number:"))
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=int(input("enter your choice:"))
if choice==1:
    print("result:",add(x,y))
elif choice==2:
    print("result:",subtract(x,y))
elif choice==3:
    print("result:",multiply(x,y))
elif choice==4:
    print("result:",divide(x,y))
