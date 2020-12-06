# CH12 Exercise 2: Change your socket program
# so that it counts the number of characters 
# it has received and stops displaying 
# any text after it has shown 3000 characters. 
# The program should retrieve the entire document
# and count the total number of characters and display the count of 
# the number of characters at the end of the document.

import socket # Import socket module
url = input("Enter URL: ") # Input socket module URL

try:
    words = url.split("/") # Split module words into string
    host = words[2]        #
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # module,
    # class, socket family, address family, module socket
    mysock.connect((host, 80)) # connect to mysock host 80
    mysock.send(("GET '+url+' HTTP/1.0\r\n\r\n").encode()) # encode 
    # and send data through default port for socket
    n =""                          # capture string
    while True:
        data = mysock.recv(512)    # define recieve data
        if (len(data) < 1):        # parameter of length
            break                  # if loop stops search at 3001 words
        n = n + (data.decode())    # n = decode data string
      
    print(n[:3001])                # print 3000 words
    print("Total Number of Characters",len(n)) # len = return total count
    mysock.close()
except:                            # when false
    print("Not Formatted Properly")