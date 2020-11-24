# Exercise 5: This program records the domain name 
# (instead of the address) where the message was sent
# from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

# method to read a file, create the required dict and return it
def processFile(filename):
    # opening file in read mode
    file = open(filename, 'r')
    # creating empty dict
    results = dict()
    # looping through each line
    for line in file:
        # checking if line starts with "From: "
        if line.startswith('From: '):
            # splitting line by space, taking second field which is the email address
            email = line.strip().split(" ")[1]
            # splitting email by "@" and extracting second field which is the domain name
            domain = email.split("@")[1]
            # if domain is already in results dict, incrementing count
            if domain in results:
                results[domain] += 1
            # else adding to dict with count=1
            else:
                results[domain] = 1
    file.close()  # closing file
    return results


# reading file name, processing file and creating dict, displaying it
filename = input("Enter a file name: ")
domains = processFile(filename)
print(domains)
# note: the order of domains on the dict may vary, and that's OK, dicts do not preserve order