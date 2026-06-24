# take a user input string and print the number of largest appearing character in it also if the string does not contain any repeated character then return zero
n = int(input("Enter the number character:"))
char = []
for i in range(0,n):
    user_char = input("Enter the string to be calculate:")
    char.append(user_char)

print("Your characters entered are:")
for i in range(0,n):
    print(char[i])

count = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(char[i] == char[j]):
            count=count+1

print(count)