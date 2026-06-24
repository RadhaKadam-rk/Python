user_input= int(input("Enter the number:"))
temp = user_input
reverse =0

while user_input>0:
    remainder = user_input % 10
    reverse =(reverse*10) + remainder
    user_input=user_input // 10


print("Reverse number is:",reverse)

if(temp == reverse):
    print("Number is palindrome number")
else:
    print("Number is not a palindrome number")
