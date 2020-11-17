
file = open("romeo.txt","r")
list = []
for line in file:
    words = line.split(" ")
    for word in words:
        if not word in list:
            list.append(word.strip())

list.sort()
print(list)