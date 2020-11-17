import sys

fname = input("Enter File Name: ")

if fname == "na na boo boo":
    print ("NA NA BOO BOO TO YOU - You have been punk'd!")
    sys.exit(0)    

fh = open(fname)
avg = 0
x = 0

# class
for lx in fh:
    # lx = lx.rstrip()
    # Skip 'uninteresting lines'
    if not lx.startswith("X-DSPAM-Confidence:"): 
        continue
    x += 1
    avg += float(lx.split()[1])

# Process our 'interesting' line 
print("Average spam confidence:", (avg/x))