# Exercise 1: Revise a previous program as follows:
# Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out 
# the person who has the most commits.
dictionary_addresses = dict()     # start variables
lst = list()

fname = input('enter file name: ') # input file name
try:
    fhand = open(fname)            # define fhand as file name
except FileNotFoundError:
    print("Cannot Open File:", fname)
    quit()

for line in fhand:
    words = line.split()            # parse the file into words
    if len(words) < 2 or words[0] !="from":
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1      # entry 1
        else:
             dictionary_addresses[words[1]] += 1    # add counts

for key, val in list(dictionary_addresses.items()):
    lst.append((val, key))     # lists value, dictionary key

lst.sort(reverse=True )         # sort by largest value

for key, val in lst[:1]:       # show only largest value
    print(key, val) 
