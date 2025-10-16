print("SHLOK KUMAR");

# # # # # # # # # # # # # # del keyword # # # # # # # # # # # # # # #  #

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Shlok")
# print(s1.name)
# del s1.name
# print(s1.name)


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

    

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.__acc_pass)

# class Person:
#     __name = "anonymous"

# p1 = Person()

# print(p1.name)

# Inheritance --))

# class car:
#     @staticmethod
#     def start():
#         print("Started...");

#     @staticmethod
#     def stop():
#         print("Stoped.")

# class TataCar(car):
#     def __init__(self, name):
#         self.name = name

# car1 = TataCar("Tata_Nano");
# car2 = TataCar("Super_Car")

# print(car1.start())

# class A:
#     varA = "welcome to class A"

# class B :
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varA)
# print(c1.varB)
# # print(c1.varC)

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("rajat")
# print(p1.name)
# print(Person.name)

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     @property
#     def percentage(self):
#          return str((self.phy + self.chem + self.math) / 3) + "%"




# std1 = Student(90, 98, 97)
# print(std1.percentage)

# std1.phy  = 85
# print(std1.percentage)


# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i + " , self.img, "j")

#     def __add__(self,num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# # num3 = num1.add(num2)
# # num3.showNumber()

# num3 = num1 + num2
# num3.showNumber()


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimenter(self):
#         return 2 * (22/7) * self.radius


# c1 = Circle(21)

# print(c1.area())
# print(c1.perimenter())


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price


    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips",20);
odr2= Order("chai",15);


print(odr1 > odr2)