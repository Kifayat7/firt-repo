light=input("entar a light ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("ready to go")
elif(light=="green"):
    print("go way")
else:
    print("there is no light bagarath:")
marks=int(input("enter  a marks"))
if(marks>=90):
    print("A+")
elif(marks>=80 and marks  <90):
    print("A")
elif(marks>=70 and marks  < 80):
    print("B")
elif(marks>=60 and marks  < 70):
    print("c")
elif(marks>=50 and marks < 60):
    print("D")
else:
    print("you are faile")
A=int(input(""))
food=input("enter a food:")
eat="yes"if food=="cake"else"no"
print(eat)
num1=int(input("enter n number 1:"))
num2=int(input("enter a munber 2:"))
sum=num1+num2
print("the sum of",num1,"and" ,num2,"is",sum,)
length=int(input("enter length of box:"))
breath=int(input("enter a brath of a box:"))
area=length*breath
print("the area of a given box is :",area,"which have length",length,"and breath is",breath,)
a=float(input("enter a number 1:"))
b=float(input("enter n number 2:"))
print("average of the given numbers is ",(a+b)//2)
a=int(input("enter a number a :"))
b=int(input("enter a number b:"))
if a>=b:
    print(True)
else:
    print(False)
