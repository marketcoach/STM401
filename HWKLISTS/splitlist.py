
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("No such file")
    quit()
lst = list()
for line in fh:
    line.rstrip()
    prepro = line.split( )
    for i in prepro:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)