class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]

    def getpassword(self):
        return self.__password
    
    def setpassword(self,password):
        self.__password=password

    @property
    def accesspost(self):
        return self._post
    
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

    def display(self):
        print(self.username,self.__password,self._post)

i=Instagram("Srinivas","Srinu@2004")
# print(i.getpassword())
# print(i.accesspost)
# print(i.display())

# Acessing Public Attributes
print(i.username)
i.username="Srinivas_k"
print(i.username)

# ACcessing Private Attributes
print(i.getpassword())
i.setpassword("Srinu")
print(i.getpassword())

# ACcessing Protected Attributes
print(i.accesspost)
i.accesspost="sunrise.png"
print(i.accesspost)
i.accesspost="Toxic.png"
print(i.accesspost)







    