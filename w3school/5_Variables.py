#Creating Variables
x = 5
y = "John"
print(x)
print(y)

#you can change the type of variable
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the Type - type() function
x = 5
y = "John"
print(type(x))
print(type(y))

#Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Multi Words Variable Names

#Camel Case(Each word, except the first, starts with a capital letter:)
myVariableName = "John"
#Pascal Case(Each word stars with a capital letter)
MyVariableName = "John"
#Snake Case(Each word is separated by an underscore character:)
my_variable_name = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Note: Make sure the number of variables matches the number of values, or else you will get an error.

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables(use print())
x = "Python is awesome"
print(x)

#also
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
