num = 19

while num != 1:
    temp = 0

    while num>0:
        var = num % 10
        temp = temp + pow(var,2)
        num = num // 10

    num = temp


if(num == 1):
    print("Happy number")
else:
    print("Not Happy number") 
