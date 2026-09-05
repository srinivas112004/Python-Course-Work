try:
    # a=int(input())
    k={1:12,12:13}
    # print(k[14])
    # l=[232,54]
    # print(l[10])
    # print(10/0)
    print('1'+1)
    print(1+"k")
except ValueError:
    print("Enter the Correct datatype")
except KeyError:
    print("Key is not there")
except IndexError:
    print("Index out of Range")
except ValueError:
    print("VAlue Error")
except ZeroDivisionError:
    print("Divison by Zer0")
except ArithmeticError:
    print("Arithmetic Error")
except TypeError:
    print("Enter the Correct datatype")
except NameError:
    print("Define var First")
else:
     pass
finally:
    print("End of the program")



try:
    # a=int(input())
    k={1:12,12:13}
    # print(k[14])
    # l=[232,54]
    # print(l[10])
    # print(10/0)
    print('1'+1)
    print(1+"k")
except (ValueError,KeyError,IndexError,ValueError,ZeroDivisionError,TypeError,NameError):
    print("Error Occured")
else:
     pass
finally:
    print("End of the program")

try:
    amt=int(input("Enter the amount :"))
    balance=amt
    if balance<0:
        raise Exception("Amount need to be positive ")
except Exception as e:
    print("Error Occured",e)
else:
     pass
finally:
    print("End of the program")


