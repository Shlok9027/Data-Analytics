print("SHLOK KUMAR");

# # # # # File I/O # # # # #

# import os
# os.remove("demo.txt")



#  Types of all text --))
                        #  1. Text File : .txt, /docs, .log etc.
                        #  2. Binary Files : .mp4, .mov, .jpeg etc.abs

#  RAM is volatile, so we need to store data in a non-volatile memory.


# f = open("Lectures_Notes\example.txt", "r")

# data = f.read()

# print(data);

# print(type(data));

# f.close()

# line1 = f.readline()

# print(line1)


# line2 = f.readline() 

# print(line2)
# f.close()

# f = open("demo.txt", "w+")
# print(f.read())
# f.write("abc")
# f.close()

# with open("practice.txt", "w") as f:
#     # f.write("Hiii  everyone\n we are learning File");
#     # f.write("using Python.\n like programming in Python")
#     data = f.read()

# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("React", "Python")
# print(new_data);


# with open("practice.txt", "w") as f:
#     f.write(new_data)

# word = "programming"

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
# #         print("FOUND")
#     else:
#         print("NOT FOUND")

#  write a function in which line of the does the word "learning " occur first. 
#  print -1 if word not found.


with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]