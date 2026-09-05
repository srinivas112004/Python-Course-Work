class whatsappv1:
    def messaging(self):
        print("You can Message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")

class whatsappv3(whatsappv2):
    def status(self):
        print("You Can add the status fro 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.status


#Multiple Inheritance

class whatsappv1:
    def messaging(self):
        print("You can Message")

class whatsappv2:
    def calls(self):
        print("You can audio and video calls")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        print("You Can add the status fro 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.status()

#Hirarchical Inheritance

class whatsappv1:
    def messaging(self):
        print("You can Message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")

class whatsappv3(whatsappv1):
    def status(self):
        print("You Can add the status fro 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.status()



#Hybrid & Multilevel  Inheritance

class whatsappv1:
    def messaging(self):
        print("You can Message")

class whatsappv2:
    def extra_msg(self):
        print("You can add wmojis, stcikers and gif's ")

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("You Can audio and video calls")
    
class whatsappv4(whatsappv3):
    def status(self):
        print("you can add the status for 24 hrs")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.extra_msg()


c=whatsappv3()
c.messaging()
c.extra_msg()
c.calls()

d=whatsappv4()
d.messaging()
d.extra_msg()
d.calls()
d.status()



class whatsappv1:
    def status(self):
        print("you can add the status for 24 hrs")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you can add Music and stickers ")
class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("you can like andd you can add reaction")
a=whatsappv3()
a.status()


class whatsappv1:
    def status(self):
        print("you can add the status for 24 hrs")
class whatsappv2:
    def status(self):
        print("you can add Music and stickers ")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can like andd you can add reaction")
a=whatsappv3()
a.status()

