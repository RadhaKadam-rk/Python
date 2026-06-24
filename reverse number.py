user_input= int(input("Enter the number:"))
temp =0
reverse =0

if user_input<0:
    reverse_num = -int(str(abs(user_input))[::-1])
    print("reverse is:",reverse_num)
else:
    while user_input>0:
        remainder = user_input % 10
        reverse = (reverse*10) + remainder
        user_input= user_input//10

    print("Reverse number is:",reverse)
