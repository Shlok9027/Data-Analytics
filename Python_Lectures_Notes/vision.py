"""def check_password(password):
    if len(password) < 8:
        raise Exception("Error : Password must be at leat 8 characters long");
    print("password is valid");

try:
    password = input("Enter your secure password : ");
    check_password(password);

except Exception as e:
    print(e) """

import os

if os.path.exists('C:/Users/shrey/SHLOK Python Code/Lectures_Notes/Lecture@9.py'):
    print("File Exists");
else:
    print("File does not Exixts")