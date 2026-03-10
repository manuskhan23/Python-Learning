# ----------------------------
# Functions and Recursion
# ----------------------------

# function

# def sum(a,b):
#     print("Sum is",a+b)

# sum(1,2)
# practice_1_list=[1,2,3,4,5,6,3,6,3,2]
# def practice_1(list):
#     print(len(list))

# practice_1(practice_1_list)

# practice_2_list=[1,2,3,4,5,6,3,6,3,2]
# def practice_2(list):
#     for i in list:
#         print(i,end=" ")
# practice_2(practice_2_list)


# def practice_3(num):
#     practictice_3_fact=1
#     for i in range(1,num+1):
#         practictice_3_fact*=i
#     print(practictice_3_fact)

# practice_3(5)

# def practice_4(usd):
#     print(usd,"usd to pkr",usd*279)
# practice_4(50)

# def practice_5(num):
#     if(num%2==0):
#         print("Even")
#     else:
#         print("Odd")

# practice_5(8)


# Recursion(A fuction which is call itself)

# def rec(n):
#     if(n==0):
#         return
#     print(n)
#     rec(n-1)
# rec(5)

# def fact(n):
#     if(n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

# def practice_6(n):
#     if(n==0):
#         return 0
#     return practice_6(n-1)+n
# practice_6_sum=practice_6(5)
# print(practice_6_sum)

practice_7_list=[1,4,3,7,2,3,6,5,8,4]
def practice_7(list,idx):
    if(idx==(len(list)-1)):
        return
    print(list[idx])
    practice_7(list,idx+1)
practice_7(practice_7_list,0)