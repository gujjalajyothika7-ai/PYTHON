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


#student scholorship eligibility checker
marks =float(input("Enter your marks:"))
attendence=float(input("Enter your attendance:"))
eligible =marks>=85 and attendence>=75
print("Sholorship elgible:",eligible)
#identity operator
a=None
print(a is none)
print(a is not none)
