# # # #question 1
# # # i=1
# # # while i<=100:
# # #     print(i)
# # #     i+=1
# # # #question 2
# # # i=101
# # # while i>=1:
# # #     print(i)
# # #     i-=1
# # # n=int(input("enter a number :"))
# # # i=1
# # # while i <=10:
# # #     print(n,"*" ,i,":",n*i)
# # #     i+=1
# # # numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# # # i=0
# # # x=5
# # # while i<len(numbers):
# # #     if(numbers[i]==x):
# # #         print("found at index :",i)
# # #     i+=1
# # i=0
# # while i<=10:
# #     print(i)
# #     if(i==3):
# #         break
# #     i+=1
# #for odd numbers 
# i=0
# while i<=10:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# #for even numbers
# i=0
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# numbers=[1,2,4,56,6,78,9,7,78,78]
# for num in numbers:
# #     print
# numbers=(1,3,45,5,64,4)
# x=5
# indx=0
# for num in numbers:
#     if (num==x):
#         print("fount the number which is at indx:",indx)
#     indx+=1
# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)
# n=int(input("enter a number :"))
# for i in range(1,10):
#     print(i*n)
# n=int(input("enter  a number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)
n=5
factorial=1
i=1
for i in range(1,n+1):
    factorial*=i
    i+=1
print(factorial)
n=int(input("enter a number to calculate a factorial:"))
fac=1
i=1
while i<=n:
    fac*=i
    i+=1
print(fac)