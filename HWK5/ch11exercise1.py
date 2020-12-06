#Ch11 Exercise 1: Write a simple program to simulate the operation
#  of the grep command on Unix. Ask the user to enter a regular 
# expression and count the number of lines 
# that matched the regular expression:

import re # re means regular expressions
pat = input("Enter A Regular Grep Expression ") # enter word/ words
                                                # grep finds the pattern
file = open("mbox.txt") # program looks in txt file
count = 0

for line in file:      # For Loop selects/ strngs each line
    line = line.rstrip() # Separate words per line
    
    if re.search(pat, line ): # If Loop selects word-obj meeting pattern
        count += 1    # Add pattern matches to the Count
print(('mbox.txt had %d that matches %s') % (count, pat)) # Prt ct match word
    # %d is count %s is entered word to  be counted

# mbox.txt 1884 lines match "Author"
# 0 lines match "mbox.txt"
# 4218 lines match java$
