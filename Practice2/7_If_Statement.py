#Python Conditions and If statements
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")

#How If Statements Work
number = 15
if number > 0:
  print("The number is positive")

#Indentation
"""
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
"""
#Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.

#Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#The Elif Keyword
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Multiple Elif Statements
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#How Elif Works
#Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#When to Use Elif
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#The Else Keyword
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Else Without Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#How Else Works
#Note: The else statement must come last. You cannot have an elif after an else.
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Complete If-Elif-Else Chain
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Else as Fallback
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#Short Hand If
a = 5
b = 2
if a > b: print("a is greater than b")

#Note: You still need the colon : after the condition.

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#This is called a conditional expression (sometimes known as a "ternary operator").

#Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#The syntax follows this pattern:
#variable = value_if_true if condition else value_if_false
#Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Practical Examples
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

#Python Logical Operators
"""
Logical operators are used to combine conditional statements. Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
"""
#The and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not Operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#Truth Tables
"""
and Operator Truth Table
Condition 1	       Condition 2	  Result
True	           True	          True
True	           False	      False
False	           True	          False
False	           False	      False
"""

"""
or Operator Truth Table
Condition 1	       Condition 2	  Result
True	           True	          True
True	           False	      True
False	           True	          True
False	           False	      False
"""

#Using Parentheses for Clarity
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

#More Examples
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

#Range checking with logical operators:
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

#Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#How Nested If Works
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


#Nested If vs Logical Operators
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#Could also be written with and:
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

#More Examples
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

#Grade calculation with nested logic:
score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

#The pass Statement
a = 33
b = 200

if b > a:
  pass
#Why Use pass?
"""
The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
"""

#pass in Development
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#pass vs Comments
#This will cause an error (empty code block):
"""
score = 85

if score > 90:
  # This is excellent
# This will raise an IndentationError
"""
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

#pass with Multiple Conditions
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#pass in Other Contexts
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet