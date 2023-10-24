name = input("Enter your full name :")
print("My name is ",name)

age = input("enter your age :")
print("I am", age, "years old")

first =input(input("enter first number"))
second =input(input("enter second number"))
third =input(input("enter third number"))

if first> second and first>third:
    print(first,"is the largest number")
elif second> first and second>third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")