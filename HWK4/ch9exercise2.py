# L Cognata
# STM-401
# 11-22-20
# Exercise 2: Write a program that categorizes each
# mail message by which day of the week the commit was
# done. To do this look for lines that start with “From”, 
# then look for the third word and keep a running count
# of each of the days of the week. At the end of the program 
# print out the contents of your dictionary 
# (order does not matter).
filename = input("Enter File Name: ")      # variable input
path = filename
(path.getcwd(),filename)
day_dict = {}

with open (path) as fin:
    for line in fin:
        line = fin.readline()

# Checks if line starts with "from"
if (line.startswith("from") or line.startswith("From") and len(line)>3):
    words = line.split(" ") # change string to list of words
day = words[2]
day_dict[day] = day_dict.get(day,0)+1
print(day_dict)