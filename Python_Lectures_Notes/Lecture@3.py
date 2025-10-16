print("SHLOK KUMAR");

# LIST --)) A built - in data type that store set of values. 
#           It can store elements of different types (integer, float, string, etc.)



# marks = [90.80, 80.20, 77.00, 81.20];

# print(marks);

# print(type(marks));

# print(marks [0]);

# print(marks [1]);

# it can store both string and nums.

# student = ["Shlok", 80.20 , 22, "Ranchi"];
# print(student[0]);
# student[0] = "Shreya";
# print(student);

# # # # # # # List Slicing --))

# marks = [90, 80, 88, 94, 80.20];

# print(marks[ 0: 5]);

# print(marks[-5 : -2]);

# # # # List Methos --))

# list = [1, 2, 3];

# list.append(4); => it can add some additional values

# print(list);

# list = [2, 3, 1, 4];

# list.sort(); => ascending order
# print(list)

# list.sort(reverse=True); => descending order
# print(list)

# list = ["s", "q", "a", "h", "s", "t", "l", "e"];
# list.sort();
# print(list);
# list.sort(reverse=True);
# print(list)

# list.reverse();  => It can totally reverse the string in ordering manner.
# print(list)

# list = [2, 5, 1, 3, 4];
# list.insert(1, 7);
# print(list);
# list.remove(2);
# print(list);

# # # # # # # # # # # Tuples in Python # # # # # # # # # # # #

# A buit - in data type that lets us create immutable sequence of Values. 


# # # # #tup = (2, 4, 6, 7, 8);
# tup = (2, )
# print(type(tup));


# print(tup)

# print(tup[1: 3])

# Write a program to ask the user to enter name of their favorite movies & store then in a list.abs

# movies = [];

# movieName_1 = input("Enter you 1st fovorite Movie : ");
# movieName_2 = input("Enter you 2nd fovorite Movie : ");
# movieName_3 = input("Enter you 3rd fovorite Movie : ");

# movies.append(movieName_1);
# movies.append(movieName_2);
# movies.append(movieName_3);

# print(movies)

# write a program to check if a list contains a palindrome of elements.(Hint: use copy() method).....

# list1 = [1, 2, 3, 4, 3, 2, 1];
# list2 = [1, 2, 3, 4, 3, 2, 1]
# list2 = [1, 2, 3, 4, 5, 6, 7];


# list1 = ["a ", "d", " t ", "w", "o"];

# list2 = ["a ", "d", " t ", "a", "o"]; 


# copy_list1 = list1.copy();

# copy_list2 = list2.copy();

# if(copy_list1 == copy_list2):
#     print("Palindrome");
# else:
#     print("NOT Palindrome")


# write a program to count the number of student with the " A " grade in the following tuple.abs

grade = [ "C", "D", "A", "A", "B", "B", "A" ];
# print(tup.count("A"));

grade.sort()
print(grade)

# grade.sort(reverse=True);
# print(grade)