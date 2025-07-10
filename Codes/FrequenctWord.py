#write a python program to find the ch1 const from the given String ("English")
line1="Hello welcome to GEC"
line2="Hello wlcome to python lab"
for word1 in line1.split():
    for word2 in line2.split():
        if word1==word2:
            print("found a common word :  ",word1)
