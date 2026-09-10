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