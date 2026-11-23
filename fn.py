#default functions
def add(a=10,b=20):
    print(a+b)
add()
#ordered parametric functions
def add(a,b):
    print(a+b)
add(6,67)

def add(a,b):
    print(a)
    print(b)
add(10,20)
#key word argumented parametric function
def add(a,b):
    print(a)
    print(b)
add(b=50,a=20)
#variable length argumented function
def add(*a):
    print(sum(a))
add(10,20,30,40,50)

a=range(1,11)
print(a)

a=range(1,11)
print(*a)
#variable length argumented function with key word arguments
def add(**a):
    print(a)
add(a=10,b=20,c=30,d=40,e=50)
a=10
print(a)
print("a")
#lambda function
add=lambda a,b:a+b
print(add(10,20))
9
square=lambda a:a*a
print(square(10))