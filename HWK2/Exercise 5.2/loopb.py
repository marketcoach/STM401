num = 0
tot = 0.0

while True :
    sval = input("Enter A Number or Enter done" )
    if sval == "done":
        break
    try:
        fval = float(sval) 
    except: 
        print("Invalid Input")
        continue
print(fval)
num = num + 1
tot = tot + fval

print("All Done")

print(max(fval) )  
print(min(fval) )
