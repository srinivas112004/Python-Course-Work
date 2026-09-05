class whatsappv1:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp - v1 {self.name}!")
    def messaging(self):
        print("You can send messages")
class Whatsappv2(whatsappv1):
    def __init__(self,name):
       self.name=name
       print(f"Welcome to the whatsapp - v1 {self.name}!")
    
    def calls(self):
        print("You can do Audio and Video Calls")
v1=whatsappv1("Srinivas")
v1.messaging()
v2=Whatsappv2("Srinu")
v2.calls()
v2.messaging()
print(v2.name)
    
