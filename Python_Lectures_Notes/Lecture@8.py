print("SHLOK KUMAR");

# # # # # # # OOP IN PYHTON # # # # # # # # 

# class and objects in python --))


# class Student:
#     name: "shlok"

# s1 = Student()

# print(s1)

# class Car:
#     color = "red";

# car1 = Car()
# print(car1.color)

# class Student :
#     name = "shlok",
#     percentage = 80.20

# s1 = Student()

# print(s1.name, s1.percentage)




# # # # # # # # _ _init_ _ Function --)) # # # # # # # # # 



# class Student:
#     name = "Shlok"
#     def __init__(self):
#         print("adding new student in Database...");

# s1 = Student()



# # # # # # # # # Class & instance Attributes # # # # # # # # #

# class Student:
#     college_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome Student")

# s1 = Student("Shlok", 93)
# s1.welcome()

## Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum  = 0
#         for val in self.marks:
#             sum += val
#         print("hii", self.name,  "Your avg score is : ",sum/3)


# s1 = Student("Shlok", [97, 94, 93])
# s1.get_avg()

# s1.name = "Shreya"
# s1.get_avg()

# s1.name = "Shubham"
# s1.get_avg()

# # # # # # # # Static Methods # # # # # # # # # #

# # Abstraction --))

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started...");
#     def stop(self):
#         self.brk = True
#         print('car is not moving')

# car1 = Car()
# car1.start()
# car1.stop()
     


#  Create Accoumd class with  attributes - balance & account no. Create for debit , credit  & print the balance.abs


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method 
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount , "was debited")
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount , "was credit")

    def get_balance(self):
        return self.balance

acc1 = Account(10000,  12345)
acc1.debit(1000)
acc1.credit(2000)