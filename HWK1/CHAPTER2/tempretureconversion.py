temperature = float(input("enter a tempreture reading in celcius "))

if temperature == 0:
    conversion = "32"
    conversion = float((1.8 * temperature) + (32) )
else:
    conversion = 1.8 * temperature + (32 )
print(str(temperature)+" celcius is: "+ str(conversion)+" farenheit.")
