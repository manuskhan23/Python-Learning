# ========================
# file input and output
# ========================
import os
# f=open("demo.txt","a")
# f.write("with")

# with open("demo.txt","a") as f:
#     f.write("45")

# ----------------
# deleting a file os.remove(file name)
# ----------------

# os.remove("demo.txt")

# practice_1=open("Practice.txt","x")
# practice_1.write("Hi everyone\nwe are learning FileI/O\nusing Java\nI like programmig Java.")

# with open("Practice.txt","r") as practice_2:
#     data=practice_2.read()
# new_data=data.replace("Java","Python")
# with open("Practice.txt","w") as practice_2:
#     data=practice_2.write(new_data)

# with open("Practice.txt","r") as practice_3:
#     data2=practice_3.read()
# print(data2.find("learning"))
count=0
with open("Practice.txt","r") as practice_4:
    data4=practice_4.read()
    num=data4.split(",")
    for val in num:
        if (int(val)%2==0):
            count+=1
print(count)
    # num=""
    # for i in range(len(data4)):
    #     if(data4[i]==","):
    #         print(num)
    #         num=""
    #     else:
    #         num+=data4[i]