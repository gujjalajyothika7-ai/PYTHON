n=int(input("Enter n"))
tem=n
sum=0
c=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**c
    n=n//10
if tem==sum:
    print(tem,"is an Armstrong number")
else:
    print(tem,"is not an Armstrong number")
#maping
a=[1,2,3,4,5]
result=list(map(lambda x:x**2,a))
print(result)
#filter
x=[1,2,3,4,5]
n=list(filter(lambda a:a%2==0,x))
print(x)
#functions with return type
def add(a,b):
    return a+b
c=add(10,20)
def sub(a,b):
    return a-b
d=sub(10,20)
print(c*d)
#write a program to perform arthematic operators using fruitful functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Input from the user
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

# Display results
#print("Addition:", add(a, b))
#print("Subtraction:", subtract(a, b))
#print("Multiplication:", multiply(a, b))

#if b != 0:
 #   print("Division:", divide(a, b))
#else:
 #   print("Division is not possible by zero")
#recursion(function calling itself)
#def fn():
#condition
#recursion call

#factorial of a number
#i=5
#t=1
#for i in range(n+1):
  #  t*=i
 #   print(t)
#factorial in recursion form
#def facta(n):
   # if n<=1:
  #      return 1
 #   return n*facta(n-1)
#print(facta(5))
#write a program to print the sum of n numbers using recurssion
#def sum_n(n):
    #if n == 0:
   #     return 0
  #  else:
 #       return n + sum_n(n - 1)
#n = int(input("Enter a number: "))
#result = sum_n(n)
#print("Sum of", n, "numbers is:", result)
#write a program to print list of fibinoci series(0,1,1,2,3,5,8,13,21)\
#scope
#c=10
#def add():
 #   a=10
  #  b=20
   # print(a+b+c)
#add()
peru="Jyothika"
def display():
    name="Jyothika"
    id=101
    print(name)
    print(id)
display()
print(peru)

naam="Jyothika"
a=10
print(id(a))

sname="Jyothika"
def sd():
    global sid
    sid=101
    global location
    location="pulivendula"
    print(sid)
    print(location)
sd()
