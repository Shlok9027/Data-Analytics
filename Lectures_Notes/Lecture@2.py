
print("SHLOK KUMAR");       

# #  String --)) It is  a data type that store a seequence of characters.
# #  "" => double quotes
# # '' => single quotes
# # """" => triple double quotes


# # #  \n => new line

# # str1 = "shlok";
# # str2 = "kumar";
# # final_str = str1 + " " + str2; 

# # print(final_str);

# # print(len(str1));

# # print(len(str2));

# # print(len(final_str));


# # str = "shlok kumar";

# # print(str[0]);
# # print(str[1]);
# # print(str[2]);
# # print(str[3]);
# # print(str[4]);
# # print(str[5]);




# # # # Slicing --)) It is a process of extracting a substring from a string.

# # str = "concationation";

# # print(str[1 : 4]); # =>onc

# # print(str[4: 7]); # => ati

# # print(str[0 : 6]); # => concat

# # print(str[6:]); # => ation

# # negative slicing --))

# # str = "mango";

# # print(str[-3 : -1]); # => ng


# # # # # # # # # # #  #String Functions --))

# str =  "i am studing python from apnacollege";

# # # # print(str.endswith("ege"));
# # # # print(str.endswith("ape"));

# # # print(str.capitalize());
# # # print(str);

# # print(str.replace("a", "o"));
# # print(str.replace("apnacollege", "chai with code"));

# # print(str.find("e"));

# # print(str.count("s"));


# name = input("Enter your name : ");
# print("length of your name is : ",len(name));

# str = "Hiii!  i am $ Shlok $ i am from ranchi $";

# print(str.count("$")



############################################ Conditional Statement ##############################################


# # # if-elif-else (SYNTAX) --))


# age = int(input("enter your age : "));

# if (age >= 18):
#     print("you are eligible to vote");

# elif(age < 18):
#       print("you are not eligible to vote");


# indentation --)) It is a space that is used to define a block of code. // proper spacing.

# marks = int(input("Enter the marks of Student : "));

# if (marks >= 90):
#     grade = "A"
# elif (marks >= 80 and marks < 90):
#     grade = "B"
# elif (marks >= 70 and marks < 80):
#     grade = "C"
# else: 
#     grade = "D"

# print("Grade of The Student  is  : ", grade);

# # # Nesting --)) It is a process of using one conditional statement inside another conditional statement.



# num = int(input("Enter the num : "));

# rem = num % 2;

# if (rem == 0):
#     print("EVEN");
# else:
#     print("ODD");


# num1 = int(input("Enter the 1st num : "));
# num2 = int(input("Enter the 2nd num : "));
# num3 = int(input("Enter the 3rd num : "));

# if (num1 > num2 and num1 > num3):
#     print("num1 is greater : ",  num1);
# elif(num2 > num1 and num2 > num3):
#         print("num2 is greater : " ,num2);
# else:
#         print("num3 is greater : ", num3);