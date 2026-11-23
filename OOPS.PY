# roots of four pillars
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

#ABSTRACTION

from abc import ABC, abstractmethod
class atm(ABC):
    @abstractmethod
    def display(self):
        pass
class bank(atm):
     def display(self):
            print("Welcome to the bank ATM")
s=bank()
s.display()

from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod  #decorator
    def withdraw(self, amount):
        pass
    def deposit(self, amount):
        pass
class BankATM(ATM):
        def withdraw(self, amount):
            print(f"Withdrawing {amount} from the bank ATM")
        def deposit(self, amount):
            print(f"Depositing {amount} into the bank ATM")
s=BankATM()
s.withdraw(1000)
s.deposit(500)

#ENCAPSULATION
class joe:
    a=10
    _b=20
    __c=30
class manasa(joe):
     def display(self):
         print("a:",self.a)
         print("_b:",self._b)
         print("__c:",self.__c)
m=manasa()
m.display()