# While Loop excute a statement numerous times so long as the condition is true
count = 100  # initialization
while count <= 105:
    print(count)
    count += 1

number = 20
while number <= 25:
    print(number)
    number += 1

# decrementing Values
    x = 10
    while x >= 1:
        print(x)
        x -= 1

# break statement
i=1
while i < 6:
    print(i)
    if i== 4:
        break # exit the entire loop
    i +=1

# continue statement

y = 1

while y <= 6:
    y +=1
    if y == 4:
        continue # skipping 4 and continues to print
    print(y)

    # For loop-help display content of variable with multiple items
    languages = ["python","PHP","Kotlin", "java"]
    for x in languages:# helps in prnting elements in sequence
       print(x)
# Range
for number in range(30, 35):
    print(number)

for a in range(6):# not specifying starting point it start from zero
    print(a)

for num in range (10,20, 2): # first starting point ,second end point number increasing by 2
    print(num)