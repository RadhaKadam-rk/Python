a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = int(input("Enter your choice:"))

if(choice==1):
    print("Addition is: ",a+b)
elif(choice==2):
    print("Subtraction is: ",a-b)
elif(choice==3):
    print("Multiplication is: ",a*b)
elif(choice==4):
    print("Division is: ",a/b)
else:
    print("Choice not found")