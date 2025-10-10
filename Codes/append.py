with open('C:\\Users\\shrey\\SHLOK Python Code\\Codes\\practice_1.txt', 'a') as file:
    content = input("Enter your new content to append : ")
    file.write(content + "\n")
    print("Content has been appended successfully")
