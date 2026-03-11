import random
import string

# # -------------------------------
# # guess the number
# # -------------------------------
# target=random.randint(1,100)

# while True:
#     UserNumber=input("Guess the number or Quit(Q): ")
#     if(UserNumber=="Q"):
#         break
#     UserNumber=input("Guess the number: ")
#     if(UserNumber==target):
#         print("Success : Correct Guess!!")
#         break
#     if(UserNumber<target):
#         print("Your Number is too small.")
#     else:
#         print("Your NNumber is too large.")

# print("-----------Game Over----------")

# ---------------------------------
# Password Generator
# ---------------------------------
characters=string.ascii_letters + string.digits + string.punctuation
password_lenght=12
password=""
for i in range(password_lenght):
    password+=random.choice(characters)
print(password)