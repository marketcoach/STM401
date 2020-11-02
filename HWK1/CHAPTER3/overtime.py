hours = float(input("How many HOURS did you work this week? "))
rate = float(input("How much are you PAID per regular time hour? "))

if hours > 40:
    overtime = hours - 40
    allpay = hours * rate + (overtime*.5 )
else:
    allpay = rate * hours

print("PAY IS: $" + str(allpay))