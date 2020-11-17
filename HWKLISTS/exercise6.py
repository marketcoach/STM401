list = []
x = input("Enter a number: ")
if x == str("done"):

    n = int(x)
    list.append(n)
    x = input("Enter a number: ")
print("Maximum: ", max(list))
print("Minimum: ", min(list))
