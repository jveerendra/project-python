from abc import ABC,abstractmethod

class ATMBase(ABC):
    @abstractmethod
    def check_balance(self):
        pass
    @abstractmethod
    def deposite(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass
    
class ATM(ATMBase):

    def __init__(self):
        self.__balance=30000
        self.transaction=[]

    def check_balance(self):
        print("your balance:",self.__balance)

    def deposite(self):
        amount=int(input("enter amount deposite:"))

        self.__balance=self.__balance+amount

        self.transaction.append("deposited"+str(amount))
        print("amount deposited successfuly")

    def withdraw(self):
        amount=int(input("enter amount dwithdraw:"))
        if amount <=self.__balance:
            self.__balance=self.__balance - amount
            self.transaction.append("withdraw"+str(amount))
            print("please take your amount")
        else:
            print("insufficient amount")

    def show_transation(self):
        print("transaction history")

        for t in self.transaction:
            print(t)

atm=ATM()

while True:
    print("\n1.deposite \n2.withdraw \n3.display \n4.transaction \n5.exit")
    choice=int(input("enter choice"))
    if choice==1:
        atm.deposite()
    elif choice==2:
       atm.withdraw()
        
    elif choice==3:
       atm.check_balance()
    elif choice==4:
        atm.show_transation()
    elif choice==5:
        print("thank for using ATM")
        break
        
    else:
        print("invalide option")
