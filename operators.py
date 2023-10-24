# arithmetic operators
x = 40
y = 12
print(x + y)
print(x - y)
print(x * y)
print(x / y) #division
print(x % y) # Modulus returns reminder after dividing two values

# comparison operators- operators used to compare values
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y) # not equal to

#assignment operators- assign a value to variables

a = 20
print(a)

b = 12
b += 2
print(b)

c = 10
c -= 3
print(c)

#logical operators have two conditions- print true if all conditions are true
num1 = 34
num2 = 67
print(num1 > num2 and num2 > num1) #print true if all conditions are true
print(num1 > num2 or num2 > num1) #print true if one condtion is true
print(not(num1 > num2 and num2 > num1)) # not reverses the results
print(not(num1 > num2 or num2 > num1)) # not reverses the results