print("Choose your condition to calculate:")
print("\n1.To find interest with given principle,rate,time\n2.To find principle with given interest,rate,time\n3.To find rate with given interest,principle,time\n4.To find time with given interest,principle,rate")

while(True):
    choice = int(input("Enter your choice:"))

    if(choice==1):
        p = float(input("Enter the principle amount:"))
        r = float(input("Enter the rate:"))
        t = float(input("Enter the time in years:"))
        print("Interest is:",(p*r*t)/100)
    
    elif(choice==2):
        r = float(input("Enter the rate:"))
        t = float(input("Enter the time in years:"))
        i = float(input("Enter the interest:"))
        print("Principle amount is:",(i*100)/(r*t))

    elif(choice==3):
        p = float(input("Enter the principle amount:"))
        t = float(input("Enter the time in years:"))
        i = float(input("Enter the interest:"))
        print("Rate is:",(i*100)/(p*t))

    elif(choice==4):
        p = float(input("Enter the principle amount:"))
        r = float(input("Enter the rate:"))
        i = float(input("Enter the interest:"))
        print("Time in year is:",(i*100)/(p*r))

    else:
        print("Choice not found.")

    user_input = input("Do you want to continue(yes/no):").lower()
    if user_input == 'no':
        break