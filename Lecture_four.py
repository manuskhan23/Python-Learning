# -----------------------
# Set and dictionary
# -----------------------

# dict={
#     "name":"Anus",
#     "age":14,
#     "Father name":"Nawab",
#     "Passion":"coding",
#     "Languages":("urdu","sindhi"),
#     "programming languages":["Javascript","HTML","CSS","SCSS","Python"],
#     "libraries and frameworks":("bootstrape","react","tailwind css","mui","sweet atert","etc")
# }
# # print(dict["programming languages"])
# dict["name"]="Huzaifa"
# dict["surname"]="huzzi"
# print(dict)

# nested_dict={
#     "name":"Ali",
#     "subjects":{
#         "eng":80,
#         "urdu":98,
#         "math":90
#     },
#     "father name":"ali kae abbu ka name"
# }
# print(nested_dict)
'''
# --------------------
# dictionary methods
# --------------------

nested_dict={
    "name":"Ali",
    "subjects":{
        "eng":80,
        "urdu":98,
        "math":90
    },
    "father name":"ali kae abbu ka name"
}

# # keys

# print(nested_dict.keys())

# # values

# print(nested_dict.values())

# # item

# print(tuple(nested_dict.items()))

# # get

# print(nested_dict.get("subjects"))

# # update

# nested_dict.update({"city":"karachi"})
# print(nested_dict)

# # clear

# nested_dict.clear()
# print(nested_dict)

# # copy

# nested_dict_copy=nested_dict.copy()
# print(nested_dict_copy)

# # fromkeys

# a=("key1","key2","key3")
# b=0

# thisdict=dict.fromkeys(a,b)

# print(thisdict)

# # pop

# nested_dict.pop("subjects")
# print(nested_dict)

# # popitem

# nested_dict.popitem()
# print(nested_dict)
'''

# ------------
# set
# ------------

# collection={3,2,2,7,4,5,"hello","anus"}
# print(collection)

# empty set

# collection2=set()
'''
# --------------
# set method
# --------------

# # add

# collection.add("happy")
# print(collection)

# # remove

# collection.remove("hello")
# print(collection)

# # clear

# collection.clear()
# print(collection)

# # pop

# collection.pop()
# print(collection)

# # union

# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))

# # intersection

# set1={1,2,3}
# set2={2,3,4}

# print(set1.intersection(set2))
'''

# dict_test={
#     "table":("a peice of furniture","list of fact and figures"),
#     "cat":"a small animal"
# }
# print(dict_test)

# set_test={"python","java","c++","python","javascript","java","python","c++","c"}
# print(len(set_test))

# student_subjects={}
# marks=int(input("Enter English marks: "))
# student_subjects.update({"English":marks})
# marks=int(input("Enter Urdu marks: "))
# student_subjects.update({"Urdu":marks})
# marks=int(input("Enter Math marks: "))
# student_subjects.update({"Maths":marks})
# print(student_subjects)

val={
    ("flooat",9.0),
    ("int",9)
}
print(val)