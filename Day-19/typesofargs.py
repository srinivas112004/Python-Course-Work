# Positional Arguments

def display(name,email,password):
    print("Name :",name)
    print("Email :",email)
    print("Password : ",password)
display("xyz","xyz@gmail.com","xyz@123")
display("xyz123","xyz@gmail.com","xyz")
display("xyz@gmail.com","xyz","xyz@123")




# Keyword Arguments

def display(name,email,password):
    print("Name :",name)
    print("Email :",email)
    print("Password : ",password)
display(name="xyz",email="xyz@gmail.com",password="xyz@123")
display(password="xyz123",email="xyz@gmail.com",name="xyz")
display(email="xyz@gmail.com",name="xyz",password="xyz@123")


# Default Arguments


def display(name,email=' ',password=' '):
    print("Name :",name)
    print("Email :",email)
    print("Password : ",password)
display("xyz","xyz@gmail.com","xyz@123")
display("xyz","xyz@gmail.com")
display("xyz")


# Variable Length Arguments

def display(*names):
    print(names)
display(1)
display(1,2,3)
display(1,2,3,4,5)



def display(**details):
    print(details)
display(Name="Srinivas")
display(Name="Srinivas",Batch=63)
display(Name="Srinivas",Batch=63,Lang="Python")

