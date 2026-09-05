from abc import ABC,abstractmethod

class Phonepe(ABC):
    def senderinfo(self):
        print("You can enter their mobile number or scanner ")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need to enter the pin")
    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepe):
    def transaction(self):
        print("Payment Using hdfc Bank")
class SBI(Phonepe):
    def transaction(self):
        print("Payment Using SBI Bank")
class UNION(Phonepe):
    def transaction(self):
        print("Payment Using UNION Bank")
class AXIS(Phonepe):
    def transaction(self):
        print("Payment Using AXIS Bank")
class ICIC(Phonepe):
    def transaction(self):
        print("Payment Using ICIC Bank")

user1=HDFC()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()

user1=SBI()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()


user1=AXIS()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()


user1=UNION()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()

user1=ICIC()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()

    
