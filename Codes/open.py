"""file = open('C:\\Users\\shrey\\SHLOK Python Code\\Lectures_Notes\\Lecture@2.py', 'r')

content = file.read()
print(content)

file.close()"""

with open('C:\\Users\\shrey\\SHLOK Python Code\\Codes\\practice_1.txt', 'w') as file:

    content = input("Enter your new Content : ")

    file.write(content)
    print("File has been written successfully");
