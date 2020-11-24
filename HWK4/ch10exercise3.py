# Exercise 3: Write a program that reads a file and 
# prints the letters in decreasing 
# order of frequency. Your program should convert 
# all the input to lower case and only count the letters a-z.
#  Your program should not count spaces, digits, punctuation, 
# or anything other than the letters a-z. 
# Find text samples from several different languages
#  and see how letter frequency varies between languages. 
# Compare your results with the tables at
#  https://wikipedia.org/wiki/Letter_frequencies.

filename = input("Enter the File Name: ") # input file name

try:
    fhand = open(filename)
except:
    print("File Name Does Not Exist!")
    quit()
# Reads the input file as a string
words = fhand.read()
# lower the characters in string. Not concerned with digits, punctuation, etc.
words = words.lower()
# separate words or string to single letters
twords = tuple(words)

letters = list()
for n in twords:
# only chooses alphabet letters

    if n.isalpha() == True:
        letters.append(n)
# Letter counting function starts.  Now count letters .

letter = dict()
for w in letters:
    letter[w] = letter.get(w,0)+1

letterf = list()

for k,v in letter.items():
    letterf.append((v,k))

letterf.sort(reverse=True)

for f,l in letterf[:]:
    print(l,f) 