# ==========================
# Loops
# ==========================

# ------------------
# While loop
# ------------------

# count=1
# while count <= 5000 :
#     print(count,"hello")
#     count += 1

# practice_1=1
# while practice_1<=100:
#     print(practice_1)
#     practice_1 +=1

# practice_2=100
# while practice_2>=1:
#     print(practice_2)
    # practice_2 -= 1

# practice_3_a=int(input("enter number for multipilation table: "))
# practice_3_b=int(input("enter number for how many multipilation table go: "))
# count2=1
# while practice_3_b>=count2:
#     print(count2,"time",practice_3_a,"is",practice_3_a*count2)
#     count2 +=1

# practice_4_list=[1,4,9,16,25,36,49,64,81,100]
# practice_4_list_len=len(practice_4_list)
# count3=0
# while count3 < practice_4_list_len:
#     print(practice_4_list[count3])
#     count3+=1

# practice_5_tuple=(1,4,9,16,25,36,49,64,81,100)
# x=64
# count4=0
# while count4 < len(practice_5_tuple):
#     if (practice_5_tuple[count4] == x):
#         print(x,"found at index",count4)
#         break
#     count4+=1

# # while loop keywords

# # break

# practice_5_tuple_b=(1,4,9,16,25,36,49,64,81,100)
# x_b=64
# count4_b=0
# while count4_b < len(practice_5_tuple_b):
#     if (practice_5_tuple_b[count4_b] == x_b):
#         print(x_b,"found at index",count4_b)
#         break
#     count4_b+=1

# # continue
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# ------------------
# For loop
# ------------------
# list=[1,2,3,4,5]

# for i in list:
#     print(i)

# practice_6_list=[1,4,9,16,25,36,49,64,81,100]
# count6=0
# for val in practice_6_list:
#     print(practice_6_list[count6])
#     count6+=1

# practice_7_list=[1,4,9,16,25,36,49,64,81,100]
# x=36
# count7=0
# for val in practice_7_list:
#     if(practice_7_list[count7]==x):
#         print("Found at index",count7)
#         break
#     else:
#         print("founding")
#     count7+=1

# ===============================
# range function in for loop
# ===============================

# for i in range(1,11,2): #(strat,end,step)
#     print(i)


# int=int(input("Enter a number: "))
# for i in range(1,11):
#     print(int*i)

# pass statement

# for i in range(10):
#     pass

# n=10
# o=0
# i=1

# for i in range(1,n+1):
#     o+=i
# print(o)
# while i<=n:
#     o+=i
#     i+=1
# print("total sum:",o)

# num=5
# factorial=1
# id=1

# while id<=num:
#     factorial*=id
#     id+=1
# print("total factorial:",factorial)

# for i in range(1,num+1):
#     factorial*= i

# print(factorial)