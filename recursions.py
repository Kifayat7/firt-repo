# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(6)


# def fac(n):
#     if(n==0) or(n==1):
#         return 1
#     else:
#         return n*fac(n-1)
    
# print(fac(5))
# i=0
# sum=0
# def sum_ofn(n):
#     if(n==0):
#         return 0
#     return sum_ofn(n-1)+n
# print(sum_ofn(5))
def print_list(list,indx=0):
    if indx==len(list):
        return 
    print(list[indx])
    print_list(list,indx+1)
num=[1,2,3,4,5,6,7,7,8,8,9]
print_list(num)