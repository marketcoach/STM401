num= 0.0
tot= 0.0
while True :
    sval = input( "Enter A Number or Enter end: " ) 
try :
    fval = float(sval) 
    continue
except : 
    print("Invalid Input")
if sval == 'end': 
    break 
print(fval)
num = num + 1
tot = tot + fval

print("All Done")
print(tot,num,tot/num)
