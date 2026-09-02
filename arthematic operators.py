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
