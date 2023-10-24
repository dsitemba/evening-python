# store multiple values
courses = ["MIT" ,"Cybersecurity", 'DataScience']
print(courses)

#Accessing elements

print(courses[1]) # index postion start from 0
print(courses[0])
print(courses[2])

# looping through array elements
for mycourse in courses: # for loop
    print(mycourse)

# Adding an element
courses.append("machine learning")
print(courses)

#removing an element from the array
courses.remove("Cybersecurity")
print(courses)