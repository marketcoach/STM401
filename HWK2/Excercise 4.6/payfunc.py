def computepay(hours, rate) :
    if hours > 40 :
        print("Compute Pay by entering your hours and rate")
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fa = float( sh )
fr = float( sr )

xp = computepay(fa,fr)
print("Returning")
print("Pay:", xp)