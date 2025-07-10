print("SHLOK KUMAR")


# # # # # # # # LOOPS # # # # # # # #

# Loops are used to repeat instruction.


# # # # #  loop --)) 

# i = 1
# while i <= 5 : 
#     print("SHLOK")
#     i += 1;

# print(i)  # => 6



# i = 5 
# while i >= 1 : 
#     print("Rev Num : ", i);
#     i -= 1


# i = 1
# while i <= 100 :
#     print(i)
# #     i += 1

# i = 100
# while i >= 1 :
#     print(i);
#     i -= 1


# num = int(input("Enter the Num : "))
# i = 1
# while i <= 10 :
#     print(i * num)
#     i += 1



# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# indx = 0
# while indx < len(list):
#     print(list[indx])
#     indx += 1


# nums =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100);

# x = 36


# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("FOUND AT idx", i)
#     i += 1



# Break --))

# i = 1
# while i <= 100:
#     print(i)
#     if(i == 20):
#         break

#     i += 1


# # # # #  # # # # # For Loop # ##  # # ##  # # # # # 


# print("End of an Loop")

# nums = [ 1, 2, 3, 4, 5]


# veg = ["potato", "brigal", "ladyffinger", "cucumber"]; 
 
# for val in veg:
#     print(val)


# tuple = ( 1, 4, 5 ,2 ,7 ,3);

# for num in tuple:
# #     print(num)

# numbers = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10];

# for num in numbers:
#     print(num);
# else: 
#         print("end")


# name = "Shlok_kumar"

# for char in name:
#     if(char == 'k'):
#         print("CHAR 'k' is FOUND")
#         break
#     print(char)
# else:
#     print("END")


#  print the element of the following list using the loop  : 
#   [1, 4, 9, 16, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 36, 49, 64, 81, 100]

# for el in nums:
#     print(el)

# search for a number x in this tuple using loop:

# x = int(input("Enter the Num : "));

# nums = (1, 4, 9, 16, 36, 49, 64, 81, 100)
# idx = 0
# for el in nums:
#     if(el == x):
#         print("Num found at idx : ", idx);
#     idx += 1


# seq  = range(10)

# for nums in seq: 
#     print(nums)

# for i in range(2, 100, 2):
#     print(i)




# for i in range(1, 101):
# print(i)

# for i in range(100, 0, -1):
# #     print(i)


# n = int(input("Enter the Num : "));

# for i in range(1, 11):
#     print(n * i)



# n = int(input("Enter the Num : "));
# sum = 0
# for i in range(1, n + 1):
#     print(i)
#     sum += i;

# print("Sum : ", sum)

# n = int(input("Enter the Num : "));

# sum = 0
# i = 1

# while i <= n:
#     sum += i;
#     i += 1;
# print("sum : ", sum)

# # # # # Factorial --))



n = int(input("Enter the Num : "));
fact = 1
i = 1

while i < n:
    fact *= i
    i += 1

print("Factorial : ", fact)