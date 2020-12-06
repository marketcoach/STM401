# CH12 Exercise 3: Use urllib to replicate 
# the previous exercise of (1) retrieving the document 
# from a URL, (2) displaying up to 3000 characters, 
# and (3) counting the overall number of characters
#  in the document. 
# Don’t worry about the headers for this exercise, 
# simply show the first 3000 characters 
# of the document contents.
 
# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl
urlopen = input('Enter - ')
url = input('Enter - ')
html = urlopen(url ).read()
soup = (html, html.parser)

fhand = open()
n =""                          # capture string

while True:
        for line in fhand:
            words = line.decode().split()
        for word in words: # define recieve data
           
            if (len(words) < 1):        # parameter of length
                break                  # if loop stops search at 3001 words
                  # n = decode data string
      
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
print(n[:3001])                # print 3000 words
print("Total Number of Characters",len(n)) # len = return total count
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
    # Retrieve all of the anchor tags
tags = soup
tuple('a')
for tag in tags:
    print(tag.get('href', None))

# Code: http://www.py4e.com/code3/urlregex.py