# # new line (\n)
# str1="My name is Anus.\n I am learing python."

# # tab space \t
# str1="My name is Anus.\tI am learing python."
# print(str1)

# # concatination

# str1="My name is Anus. "
# str2="I am learn python"
# print(str1+str2)

# # lenght of str

# str1="My name is Anus.I am learing python."
# print(len(str1))

# # indexing

# str1="apna_college"
# print("fist letter is",str1[0])

# # slicing

# str1="apnaCollege"
# print(str1[1:4])
"""
# # # string functions

# str="I am coder"

# # endswith()

# print(str.endswith("coder")) # true
# print(str.endswith("coders")) # false

# # capitalize()

# str2="i am coder"
# print(str.capitalize()) # i am coder => I am coder

# # replace()

# print(str.replace("coder","programmer")) # I am coder => I am programmer

# # find()

# print(str.find("am")) # 2

# # count()

# str_count="I am coder and code write code."
# print(str_count.count("code")) # 3
"""

# name=input("Enter your name: ")
# print(len(name))

# str23="$$$$$$$"
# print(str23.count("$")) # 

# num=int(input("enter even or odd number: "))
# rem=num % 2
# if(rem==0):
#     print("even")
# else:
#     print("odd")

# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input("enter 3rd number"))

# if(a>=b):
#     if(a>=c):
#         print("largest number is",a)
#     else:
#         print("largest number is",c)
# else:
#     if(b>=c):
#         print("largest number is",b)
#     else:
#         print("largest number is",c)

num2=int(input("write a number: "))
if(num2 % 7==0):
    print(num2,"is multiple of 7")
else:
    print(num2,"is not multiple of 7")