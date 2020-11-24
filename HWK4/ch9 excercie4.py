# Exercise 4: Add code to the above program to figure out 
# who has the most messages in the file. After all the
# data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who 
# has the most messages and print how many
# messages the person has.
def read_input(filename):      # function and variable
    file=open(filename,'r')    # open and read file
    list1=file.readlines()
    file.close()               # closes file
    # variables
    max=0
    name=""
    dict1={}
    # for loop
    for i in list1:
        list2=i.split(" ")
        if(list2[-1:-2]=="\n"):
            dict1[list2[0]]=list2[1][0:len(list2[1]-2)]
        else:
            dict1[list2[0]] = list2[1]
    # for loop sets max = to value if value > max
    for val in dict1.items(): 
        val=int(val)
        if(val>max):
            max=int(val)
    # for loop add key1 to name if value1 = max
    for key1, val1 in dict1.items():
        val1=int(val1)
        if(val1==max):
            name+=key1
    print(name,max)
    
n=input("Enter file name with extension:")
read_input(n)