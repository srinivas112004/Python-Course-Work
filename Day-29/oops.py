class Flipkart:
    products={'shirts':1000,'shoes':12000,'Suits':30000}
    
    discount=30

    # def __init__(self,name,phone,address):
    #     self.name=name
    #     self.phone=phonew5
    #     self.address=address

    @classmethod
    def display(cls):
        print(cls.products)
    
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name}, Welcome to the flipkart ")

    @staticmethod
    def discount_count():
        print(f"Discount is {Flipkart.discount}% on all the products  ")

User1=Flipkart()
User1.userinfo("Srinivas",6320156646,"Hyd")
User1.display()
User1.discount_count()

User2=Flipkart()
User2.userinfo("Rajesh",6320159946,"Noida")
User2.display()
User2.discount_count()

User3=Flipkart()
User3.userinfo("Sruesh",6320786646,"Chennai")
User3.display()
User3.discount_count()

# USing Class Name we can access -> cls Methods,static Method and class attributes
# Using Object referecne -> instance Method,class method, Static Method ,Class Attribite ,Instannce Attribute