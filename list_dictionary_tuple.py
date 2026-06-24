#Create a list
mylist = []

#Display the empty list
print("The list is:",mylist)

#enter the character/number in list
n = int(input("Enter the number to put in string:"))
for i in range(0,n):
    user_in = input("Enter the character or number or string in list:")
    mylist.append(user_in)

print("Your list is")
for i in range(0,n):
    print(mylist[i])

#Create a Dictionary
mydict = {}

#Display the empty dictionary
print("Dictionary content is:",mydict)

#Display the content in dictionary of your choice
mydict1 = {"name":"A","roll_no.": 1}
print(mydict1)

#creating a tuple
mytuple = ()

#Display the empty tuple
print("Tuple content is:",mytuple)

#Display the content in tuple by your choice
mytuple1 = (1,2,'a',3)
print(mytuple1)