num = 0
tot = 0.0
while True :
    sval = input('Enter A Number: ') 
    if sval == 'done' :
        break
    try: 
        fval = float(sval)
    except: 
        print('Invalid input')
    continue
    #print (fval) 
num = num + 1
t0t = tot + fval

#print ('All Done')
print (tot,num,tot/num)