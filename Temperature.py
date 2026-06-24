#Menu Table
print("\n1.To Calculate Temperature in Celsius\n2.To Calculate Temperature in Fahrenheit\n3. To Calculate Temperature in Kelvin")

while(True):
    choice1 = int(input("Enter your choice:"))
    if(choice1 == 1):
        choice2 = int(input("Choose the temperature name you are going to enter \n1.Fahrenheit\n2.Kelvin"))
        if(choice2 == 1):
            fahrenheit = float(input("Enter the value of Fahrenheit:"))
            print("Value in celsius is:",(fahrenheit-32)*5/9)
        elif(choice2 == 2):
            Kelvin = float(input("Enter the value of Kelvin:"))
            print("Value in Celsius is:",Kelvin-273.15)
        else:
            print("Wrong choice.")
        
    elif(choice1 == 2):
        choice2 = int(input("Choose the temperature name you are going to enter \n1.Celsius\n2.Kelvin"))
        if(choice2 == 1):
            Celsius = float(input("Enter the value of degree celsius:"))
            print("Value in Fahrenheit is:",(Celsius*9/5)+32)
        elif(choice2 == 2):
            Kelvin = float(input("Enter the value of Kelvin:"))
            print("Value in Fahrenheit is:",((Kelvin-273.15)*9/5)+32)
        else:
            print("Wrong choice.")

    elif(choice1 == 3):
        choice2 = int(input("Choose the temperature name you are going to enter \n1.Fahrenheit\n2.Celsius"))
        if(choice2 == 1):
            fahrenheit = float(input("Enter the value of Fahrenheit:"))
            print("Value in celsius is:",((fahrenheit-32)*5/9)+273.15)
        elif(choice2==2):
            Kelvin = float(input("Enter the value of Kelvin:"))
            print("Value in Celsius is:",Celsius+273.15)
        else:
            print("Wrong choice.")

    else:
        print("Choice not found.")

    user_input=input("Do you want to continue(yes or no):").lower()
    if(user_input == 'no'):
        break