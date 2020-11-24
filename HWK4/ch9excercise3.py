# L Cognata
# STM-401
# 11-22-20
# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many 
# messages have come from each email address, and print the dictionary.

#prompt the user for filename
filename = input("Enter file name:\t")
#open the file in read mode
f = open(filename, "r")
#read all the lines from the file
lines = f.readlines()
#create an empty dictionary
d = {}
#iterate over the lines
for line in lines:
   #strip the line
   line = line.strip("\n")
   #split the line using space
   vals = line.split(" ")
   #if the length of the list is 8 and the first keyword is from
   if(len(vals) == 8 and vals[0] == "From"):
       #check whether email already present in the dictionary
       #if not add it as a new value
       if vals[1] not in d:
           d[vals[1]] = 1
       #increment the current value
       else:
           d[vals[1]] += 1
#print the dictionary
print(d)
#initialise the maximums
max_val = 0
max_mail = ""
#iterate over the dictionary
for mail in d:
   #if the count of the mails is greater than current max val, update the max val and max-mail
   if(d[mail] > max_val):
       max_val = d[mail]
       max_mail = mail
#print the output
print(max_mail + " " + str(max_val))