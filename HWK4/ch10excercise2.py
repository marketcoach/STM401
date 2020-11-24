# Exercise 2: This program counts the distribution of the 
# hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string 
# and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts,
# one per line, sorted by hour as shown below.

dictionary_hours = dict()     # start variables
lst = list()

fname = input("Enter File Name: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("Cannot Open File:", fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != "from": # set the from line
        continue

    col_pos = words[5].find(":")              # find time string and split it
    hour = words[5][:col_pos]
    if hour not in dictionary_hours:
        dictionary_hours[hour] = 1      # first entry
    else:
        dictionary_hours[hour] += 1     # add counts

for key, val in list(dictionary_hours.items()):
    lst.append((key, val))              # lists hours and count

    lst.sort()                          # sort by hour

    for key, val in lst:
        print(key, val) 
