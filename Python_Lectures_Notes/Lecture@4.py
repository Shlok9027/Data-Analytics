print("SHLOK KUMAR");

# info = {
#     "name" : "Shlok_Kumar",
#     "subject" : "Python",
#     "age" : 22,
#     "is_adult" : True,
#     "marks" : 80.20

# }
# print(info);        


# null_dict = {}
# print(null_dict)


# # # # # Nested Dictionaries --))


# student = {
#     "name" : "SHLOK",
#     "age" : 22,
#     "branch" : "CSE(AIML)",
#     "subjects": {
#         "maths" : 92,
#         "science" : 88,
#         "english" : 75,
#     }
# }
# print(student["subjects"]["maths"]);


# # # # # Dictionary Methods # # # # #



# student = {
#     "name" : "SHLOK",
#     "age" : 22,
#     "branch" : "CSE(AIML)",
#     "subjects": {
#         "maths" : 92,
#         "science" : 88,
#         "english" : 75,
#     }
# }

# print(student.keys());



# info = {
#     "name" : "shlok_kumar",
#     "subjects" : ["python", "java", "c"],
#     "topics" : ("dict", set),
#     "age" : 22,
#     "is_adult" : True,
#     12.99 : 94.99
# }
# print(info["name"])

# info["name"] = "shreya_kumari";
# print(info)


# new.dict.


# Set in python --))

# collections  = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5,  "Hiii", "hehehehe"}

# print(collections);
# print(type(collections))
# print(len(collections))

# # To create empty set -

# set = set();
# print(set)

# # Set methods --))
#                     1.set.add(el)    => add an element
#                     2.set.remove(el) => removes the elem an 
#                     3.set.clear()    => empties the set
#                     4.set.pop()      => removes a random value
#                     5.set.union(set2) => combines both set values & return new
#                     6.set.intersection(set2) => combines common values & return new
# collection = set()

# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("abc")


# collection.remove(3)
# print(collection)

# print(type(collection))


# values = { "hello" , "hiii", "python", "java", "coding"}

# print(values.pop())


# UNINON --))

# set1 = {1, 2, 3}
# set2 = {3, 3, 5}

# print(set1.union(set2))
# print(set1);
# print(set2)

# print(set1.intersection(set2))

# # # store the following word meaning in python dictionary:
    #  table : " a piece of furniture", "list of facts & figures"
    #  cat : " a small animal"


# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "lists of facts & figures"]
# }
# print(dictionary)

# # # your are given a list pf sunjects for student.Assume one classroom id required for 1 subject. How many classroom are needed by all students.
    # "python", "java", " C++", "python", "javascript",
    # "java", python, "java", "C++", "C"

# subjects = {
#     "python", "java", "C++", "python", "javascript",
#     "java", "python", "java", "C++", "C"
# }

# print(subjects)

# print(len(subjects))


# # # WAP to enter marks of 3 subjejcts from the user and store them in a dictionary. Start with an empty dictionary & add one by one . Use 
#    subject name as key & marks as value.


# marks = {}

# x = int(input("enter math : "));

# marks.update({"math" :  x})

# y = int(input("enter science : "));

# marks.update({"sci" : y})

# z = int(input("enter english : "))

# marks.update({"eng" : z})


# print(marks)


values = {
       ("int", 9),
       ("float", 9.0),
}


print(values)