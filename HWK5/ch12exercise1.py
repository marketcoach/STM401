#  Exercise 1: Change the socket program socket1.py 
# to prompt the user for the URL so it can read any web page. 
# You can use split('/') to break the URL into
#  its component parts so you can extract the host name 
# for the socket connect call. 
# Add error checking using try and except to handle 
# the condition where the user enters an improperly 
# formatted or non-existent URL.

import urllib.request #  go to web url entered in input
try :
    user_url = input("Enter url:") # User Input
    web_url = urllib.request.urlopen(user_url) # open url
    seq=user_url.split('/') # split url '/'
    print("Host name is =" ,seq[2]) # 2nd element splitted list is hostname
                                    # so host name prints
except:
    #Enter url once more if 1st entry is not valid
    print("URL Entered is not Valid Please Enter URL Again ONCE!")

   #  correct entry format  https://www.yahoo.com 