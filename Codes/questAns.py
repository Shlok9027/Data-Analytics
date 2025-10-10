# Write a program that iterates through a list of numbers and prints whether each number is even or odd.


"""list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for num in list:
    if num % 2 == 0:
        print(f"{num } is even");
    else:
        print(f"{num} is odd")"""


# Write a function that takes a list and returns a new list with all duplicate elements removed.


"""def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1,2,3,4,5,5,6]

correct_list = remove_duplicates(input_list)
print(correct_list)  # Output: [1, 2, 3, 4, 5, 6]"""

# Develop a function that checks if a given string is a palindrome.
"""
def is_palidrome(s):
    cleaned_s = s.replace(" ","").lower()

    return cleaned_s == cleaned_s[::-1]

print(is_palidrome("A Man a plan a canal panam")) #true
print(is_palidrome("kumar")) # false"""



# Write a program to count the frequency of each element in a list and store the result in a dictionary.

#  dictionary have their own key and value pair

"""def count_frequency(input_list):
    frequency_map = {}
    for item in input_list:
        if item in frequency_map:
            frequency_map[item] +=1
        else:
            frequency_map[item] = 1
    return frequency_map
my_list = [1,2,31,4,2,1,1,3,4,"apple", "banana","orange", "apple"]

frequency = count_frequency(my_list)

print(frequency)  # Output: {1: 3, 2: 2, 3: 2, 4: 2, 'apple': 2, 'banana': 1, 'orange': 1}"""


# Write a recursive function to calculate the factorial of a number.


"""def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    

n = int(input("Enter a number : "))

print(f"The Factorial of {n} is {factorial(n)}  " )
"""


#  Define a class for a Car with attributes like make, model, and year. Include methods to start and stop the engine.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_start = False


        def start_engine(self):
            if not self.is_engine_start:
                self.is_engine_start = True
                print(f" The engine of {self.make } {self.model} has started...")
            else:
                print(f"The engine of {self.make} {self.model} is already running...")

        def stop_engine(self):
            if self.is_emgine_start:
                self.is_engine_start = False
                print(f"The engine of {self.make} {self.model} has stopped...")
            else:
                print(f"The engine of {self.make} {self.model} is already stopped...")

car1 = Car("Toyota", "fortuner", 2020)

car2 = Car("mercedes", "rx", 2021)


car1.start_engine()
car1.stop_engine()

car2.start_engine()
car2.stop_engine()