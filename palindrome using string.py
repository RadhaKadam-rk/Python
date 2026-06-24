user_input = input("Enter the string:")
temp = user_input
reverse = 0
i=0

while i<len(user_input):
    reverse = user_input[::-1]
    i+=1

if(temp == reverse):
    print("String is palindrome")
else:
    print("String is not a palindrome")