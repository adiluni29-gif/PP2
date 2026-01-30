#Python Operators
#In the example below, we use the + operator to add together two values:
print(10 + 5)

#Although the + operator is often used to add together two values, like in the example above, it can also be used to add together a variable and a value, or two variables:
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#Arithmetic Operators
"""
Operator	Name	                Example	
+	        Addition	            x + y	
-	        Subtraction	            x - y	
*	        Multiplication	        x * y	
/	        Division	            x / y	
%	        Modulus             	x % y	
**	        Exponentiation	        x ** y	
//	        Floor division	        x // y
"""
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Division in Python
#/ - Division (returns a float)
#// - Floor division (returns an integer)
x = 12
y = 5

print(x / y)

#It rounds DOWN to the nearest integer:
x = 12
y = 5

print(x // y)

#Assignment Operators
"""
Operator	Example	         Same As	
=	        x = 5	        x = 5	
+=	        x += 3          x = x + 3	
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3	
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=	        x >>= 3       	x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 3)   x = 3
                            print(x)
"""

#The Walrus Operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison Operators
"""
Operator	Name	                    Example	
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y
"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Chaining Comparison Operators
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Logical Operators
"""
Operator	Description	                                                   Example	
and 	    Returns True if both statements are true	                   x < 5 and  x < 10	
or	        Returns True if one of the statements is true	               x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	not    (x < 5 and x < 10)
"""

x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))

#Identity Operators
"""
Operator	   Description	                                               Example	
is 	           Returns True if both variables are the same object	       x is y	
is not	       Returns True if both variables are not the same object	   x is not y
"""

#The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#The is not operator returns True if both variables do not point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Difference Between is and ==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Membership Operators
"""
Operator	Description	                                                                         Example
in 	        Returns True if a sequence with the specified value is present in the object	     x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	 x not in y
"""

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise Operators
"""
Operators   Name	                    Description	                                                                                             Example	
& 	        AND	                        Sets each bit to 1 if both bits are 1                  	                                                 x & y	
|	        OR	                        Sets each bit to 1 if one of two bits is 1	                                                             x | y	
^	        XOR	                        Sets each bit to 1 if only one of two bits is 1	                                                         x ^ y	
~	        NOT	                        Inverts all the bits	                                                                                 ~x	
<<	        Zero fill left shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off	                     x << 2	
>>	        Signed right shift	        Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off  x >> 2
"""
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

#Precedence Order
"""
Operator	                                           Description	
()	                                                   Parentheses	
**	                                                   Exponentiation	
+x  -x  ~x	                                           Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                                           Multiplication, division, floor division, and modulus	
+  -	                                               Addition and subtraction	
<<  >>	                                               Bitwise left and right shifts	
&	                                                   Bitwise AND	
^	                                                   Bitwise XOR	
|	                                                   Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	       Comparisons, identity, and membership operators	
not	                                                   Logical NOT	
and	                                                   AND	
or	                                                   OR	
"""
#Left-to-Right Evaluation
#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)
