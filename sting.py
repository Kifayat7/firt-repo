"""str1="this is apna colloage .\nAnd it is veru best"
print(str1)
str1=("this is apna colloage ")
str2=("and it is very best")
final_str=str1+str2
print(len(str1))
print(len(str2))
print(final_str)
str1="kifayat"
str2="hussain"
print(str1+" "+str2)
print(str1[1])
name="kifayat hussain"
print(name[0:16])
print(name.count("a"))
print()
num=5
if(num>2):
    print("greater than 2")
if (num>3):
    print("greate than 3")
if (num>6):
    print("less than 6")
else:
    print("less than 6")
number=int(input("enter a number "))
if(number%2==0):
    print("even")
else:
    print("odd4")
number1=int(input("enter a number 1:"))
number2=int(input("enter a number 2:"))
number3=int(input("enter a number 3:"))
if (number1>number2 and number1>number3):
    print("number 1  is greater than")
elif(number2>number1 and number2>number3):
    print("number 2 is grater than 1")
else:
    print(number3)"""
numb=int(input("enter a number "))
if (numb%7==0):
    print("the given number is multiple of 7")
else:
    print(numb,"is not multiple of 7")