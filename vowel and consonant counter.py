# take user input string and count vowels in it
user_input = input("Enter your string:").lower()
count_vow = 0
vowel = ['a','e','i','o','u','A','E','I','O','U']

for i in range(0,len(user_input)):
    for j in range(0,len(vowel)):
        if (user_input[i] == vowel[j]):
            count_vow = count_vow + 1

print("Vowel count is:",count_vow)