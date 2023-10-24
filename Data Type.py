# Datatype
number = 100  # int
second = 56.78  # float
text = "Helo there"  # str
isinteresting = True  # bool

Cars = ["toyota", "Nissan", "VW"]  # list
print(Cars)

fruits = ("banana", "oranges", "apple")  # Tuple

Countries = {"Kenya" , "Ethiopia", "Tunisia"} #set
print(Countries)

details= {
    "firstname" : "Glory",
    "age":34,
    "course": "MIT",
    "nationality": "Kenya",
} # Dictionary- Has key and value

print(details)
print(details["course"])# to print out a value you mention the key
print(details["nationality"])

print(fruits)
print(number)
print(second)
print(text)
print(isinteresting)
print(number, "is an integer")

# Determining Data type
print(type(number))
print(type(second))
print(type(isinteresting))

# Typecasting-Coverting one data type into another
print(float(number))
print(int(second))
