'''
M1_OtherFunctions.py
Who has access
A
System properties
Type
Text
Size
589 bytes
Storage used
589 bytes
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
16 Sept 2022 by Akash Chauhan
Opened
06:10 by me
Created
29 Sept 2022
No description
Viewers can download
'''
def add(x,y):
    '''This function adds two variables a and b
    and returns the sum of a and b
    '''
    return x+y

def sub(x,y):
    '''This function substracts two variables a and b
    and returns the substraction of a and b
    '''
    return (x-y)

#print("Hello world 1")

def main():
    '''This function is testing all the functionalities
    '''
    if add(1,2) == 3:
        print("Add functionality is wotking fine!")
    if sub(3,2) == 1:
        print("sub functionality is wotking fine!")

#print(__name__)

if __name__ == "__main__":
    main()

#print("Hello world 3")
'''
M1_Task_01_VariablesInPython.py
Who has access
A
System properties
Type
Text
Size
655 bytes
Storage used
655 bytes
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
14 Sept 2022 by Akash Chauhan
Opened
06:10 by me
Created
29 Sept 2022
No description
Viewers can download
# Declaration of a variable is not required in python
# M1_Task-01_VariablesInPython


Declaration of a variable is not required in python
Declaration of a variable is not required in python
Declaration of a variable is not required in python
'''

x = 5
y = "John"
print(x)
print(y)

# Over written feature of python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# Casting of a value
x = str(321)  # x will be "321"
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

# Python string/character storage!
# double quote and single quote
x = "John"
x = 'John'
x = 'b'
x = "b"


print(x)
'''
M1_Task_03_MainFunctionInPython.py
Who has access
A
System properties
Type
Text
Size
133 bytes
Storage used
133 bytes
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
16 Sept 2022 by Akash Chauhan
Opened
06:11 by me
Created
29 Sept 2022
No description
Viewers can download
'''
# Main function

import M1_OtherFunctions

print(M1_OtherFunctions.add(1,2)) 
print(M1_OtherFunctions.sub(3,1)) 

'''
Output:
3
2
'''

'''
M1_Task_04_DatatypesInPython.py
Who has access
A
System properties
Type
Text
Size
1 KB
Storage used
1 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
26 Sept 2022 by Akash Chauhan
Opened
06:12 by me
Created
29 Sept 2022
No description
Viewers can download
'''
# Varibale is like a container
var1 = 123
var2 = 123.4
var3 = "Hello"

print(var1)
print(var2)
print(var3)

# Casting of a value
x = str(321)  # x will be "321"
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)


# Python string/character storage!
# double quote and single quote
x = "John"
x = 'John'
x = 'b'
x = "b"
x = """Akash"""
x = '''Akash'''

print(x)

# type of varaible
var1 = 123
var2 = 123.4
var3 = "46"

print(type(var1))
print(type(var2))
print(type(var3))

print(var1 + var2)
# print(var2 + var3) #Error, can not add string with integer
print(str(var2) + var3)
print(var2 + int(var3))

print("Hello world\n" * 10)
print(10*5)

#How about an integer
print(10 * str(var1 + var2))

#Take input from the user
print("Enter the value of a")
a = input()
b = input("Value of a ")
#print(a+10)    #Error
print(int(a)+10)

'''
Data Types:
1- Numeric:
   int
   float
2- Binary, Octal and Hexadecimal
   n1 = 0B0101010 # [0B for Binary{0,1}]
   n2 = 0O17      # [0O for octal{0,1,2,3,4,5,6,7}]
   n3 = 0X1c2     # [0X for hexadecimal{0-9,A,B,C,D,E,F}]
3- Bool data type:
   a  = 10
   b  = 20
   if(a<b): print("Hello") 
'''

n1 = 0B0101010
n2 = 0O17
n3 = 0X1c2

print(int(n1))
print(int(n2))
print(int(n3))

print(int('0101010',2))
print(int('17',8))
print(int('1c2',16))

# Bool data type
a  = 10
b  = 20
c  = a<b 
if(c): print("Hello") 

a = 5>10
print(a)
'''
M1_Task_05_ArithmeticOperatorAndExpressionInPython.py
Who has access
A
System properties
Type
Text
Size
1 KB
Storage used
1 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
21 Sept 2022 by Akash Chauhan
Opened
06:12 by me
Created
29 Sept 2022
No description
Viewers can download
'''
#Arithmetic Operator
'''
Addition [+]
Subtraction [-]
Multiplication  [*]
Division    [/]
Modulus [%]
Exponentiation  [**]
Floor division  [//]
'''
# M1_Task-05_ArithmeticOperatorsAndExpressionsInPython.py

val1 = 2
val2 = 3

res = val1 + val2
print(res)

res = val1 - val2
print(res)

res = val1 * val2
print(res)

res = val1 / val2
print(res)

# Modulus Operator
res = val1 % val2
print(res)

# Exponentiation Operator 
# raise the first operand to power of second
res = val1 ** val2
print(res) # 2^3

# Floor division
res = val1 // val2
print(res)  # 0 not .66

# Expression

#Constant Expressions:
x = 15 + 1.3
print(x)

#Arithmetic Expressions:
x = 40
y = 12
add = x + y
print(add)

#Integral Expressions:
a = 13
b = 12.0
c = a + int(b)
print(c)

#Floating Expressions:
a = 15
b = 5
c = a / b
print("a / b", c)

#Relational Expressions:
a = 21
b = 13
c = 40
d = 37

# >=, <=, >, <, !=, == -> True/False

p = (a + b) >= (c - d)
print(p)    # True

#Logical Expressions:
P = (10 == 9)
Q = (7 > 5)

R = P and Q
S = P or Q
T = not P

print(R)
print(S)
print(T)

'''
M1_Task_06_CalculatorInPython.py
Who has access
A
System properties
Type
Text
Size
837 bytes
Storage used
837 bytes
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
16 Sept 2022 by Akash Chauhan
Opened
06:12 by me
Created
29 Sept 2022
No description
Viewers can download
# Create a calculator in python 
# and along with that test all the functionalities you have created
'''
def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multi(a,b):
    return (a*b)

def div(a,b):
    return (a/b)

def expo(a,b):
    return a**b

def floorDiv(a,b):
    return a//b


def main():
    if add(10,20) == 30:
        print("add functionality is working fine\n")

    if sub(30,20) == 10:
        print("sub functionality is working fine\n")

    if multi(3,6) == 18:
        print("multi functionality is working fine\n")

    if div(40,20) == 2:
        print("div functionality is working fine\n")

    if expo(2,2) == 4:
        print("expo functionality is working fine\n")
    
    if floorDiv(5,2) == 2:
        print("floorDiv functionality is working fine\n")


if __name__ == "__main__":
    main()
'''
M1_Task_07_PrimeOrNotInPython.py
Who has access
A
System properties
Type
Text
Size
1 KB
Storage used
1 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
21 Sept 2022 by Akash Chauhan
Opened
06:13 by me
Created
29 Sept 2022
No description
Viewers can download
'''
# M1_Task-07_PrimeOrNotInPython

# o(n)
import math
from re import A

def primeOrNor1(x):

    count = 0
    y = int(x)
    for i in range(2,y-1):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime"

# o(n/2)
def primeOrNor2(x):

    count = 0
    y = int(x)
    for i in range(2,y//2):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime"


# o(sqrt(n))
def primeOrNor3(x):

    count = 0
    y = int(x)
    r = math.ceil(math.sqrt(y)) # sqrt1(y)
    print(r)
    for i in range(2,r+1):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime"           


def sqrt1(x):

    i = 1
    r = 1
    while(r < x):
        r = i*i
        i=i+1

    return i-1

def primeOrNor4(x):

    count = 0
    y = int(x)
    r = sqrt1(y)
       
    for i in range(2,r+1):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime" 

x = input("Enter the value of x: \n")
primeOrNor1(x)
# primeOrNor2(x)
# primeOrNor3(x)
# primeOrNor4(x)
'''
M1_Task_08_StringInPython.py
Who has access
A
System properties
Type
Text
Size
3 KB
Storage used
3 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
28 Sept 2022 by Akash Chauhan
Opened
06:13 by me
Created
29 Sept 2022
No description
Viewers can download
'''


'George'

"George"

print ('George')

print ("George")

x4 = "George"

""
''
""""""
''''''

x4

y = 10
print (y + "Dollars")

y = 10
print (str(y) + " Dollars")

'I'm fine'

"I'm fine"

# Escape a character
'I\'m fine'

'Press "Enter"'

'Red' 'car'

'Red ' 'car'

'Red ' + 'car'  # concating two strings in python

print ('Red ' + 'car')

print ('Red', 'car', 123)

print (3,5)

3, 5, 6.9, 7.0, 'car'


'''
Syntax:
    slice(stop)
    slice(start, stop, step)
'''

# String slicing
String = 'ASTRING'

# ASTRING
# 0123456
# -7-6-5-4-3-2-1
 
# Using slice constructor
print("String slicing")
# print(String[slice(3)])
# print(String[slice(1, 5, 2)])
# print(String[slice(-1, -8, -2)])

# print(String[-2])


'''
Syntax:
    s[index]
    s[start, stop]
    s[start, stop, step]
'''
String[0]
String[2::]
String[::2]
String[:4:]

String[-4:-1]
String[-1:-4:-1]

# Repeating a string
print((String+'\n') * 10)
print(123 * 10)















# '''''' and """""" can also be used to represent a string

s = """Hello World""" # docstring
print(s)


# String length
l = len(s)
print(l)


# compare two strings
s1= "helloo"
s2= "hello"

if s1 == s2:
    print("Equals")
else:
    print("Not Equals")

if s1 <= s2:
    print("s1 is smaller than or equal to s2")
else:
    print("s2 is smaller than s1")


# Removing space from the string
name = " Akash Chauhan "
print(name.rstrip())
print(name.lstrip())
print(name.strip()) # Remove both left and right spaces from the string
print(name)







# Find a substring
str = input("Enter main string: ")
subStr = input("Enter sub string: ")

n = str.find(subStr,0,len(str))

if n == -1:
    print("Substring not found")
else:
    print("Substring found at position",n)






# Strings are Immutable in Python: 
"""
An immutable object is a object whose content can not be changed
In python: strings, numbers and tuples are immutable
"""

s1 = 'one'
s2 = 'two'

s1 = s2

print(s1)


# Replacing a substring
str = "That is beautiful"
s1 = 'beautiful'
s2 = 'not beautiful'

str1 = str.replace(s1,s2)
print(str1)







# Converting strings to numbers 
str = "25"
number = int(str)
print(number)

# Converting numbers to strings
str2 = str(number)
print(str2)



# Split function 
str = "That is beautiful"
str1 = str.split(' ')
print(str1) 

for i in str1:
    print(i)



# changing case of a string
str = "That is beautiful"
print(str.upper())
print(str.lower())
print(str)




# Superscript and Subscript concept in Python
numbers_to_letters = str.maketrans("123", "ABC")
print("Question 1, point 2 and 4".translate(numbers_to_letters))

# subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
# print("C2H5OH".translate(subscript))

# superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# print("PIr2".translate(superscript))

# superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# print("PIr2".translate(superscript).replace('PI', 'π'))

'''
M1_Task_09_StatementsInPython.py
Who has access
A
System properties
Type
Text
Size
2 KB
Storage used
2 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
28 Sept 2022 by Akash Chauhan
Opened
06:13 by me
Created
29 Sept 2022
No description
Viewers can download
from re import A, L
'''

x = int(input("Please enter an integer: "))

# If else statement
if x < 0:
    print('less than zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# For statements [The range() Function]
for i in range(1,5):
    print(i)

x = 5
# While loop statement [Values in reverse order]
while(x >= 1):
    print(x)
    x=x-1


# break and continue Statements, and else Clauses on Loops

n = 8
count  = 0
for x in range(2, n):
    if n % x == 0:
        print("Not a prime")
        count  = count+1
        break
    else:
        continue
if count == 0:
    print("It is a prime number")


# The pass statement does nothing. 
# It can be used when a statement is required syntactically 
# but the program requires no action.
def initlog():
    pass   # Remember to implement this!

initlog()

# while True:
#     pass





# match Statements
cpuModel = str.lower(input("Please enter your CPU model: "))
 
# The match statement evaluates the variable's value
match cpuModel:
    case "celeron": 
        print ("Forget about it and play Minesweeper instead...")
    case "core i3":
        print ("Good luck with that ;)")
    case "core i5":
        print ("Yeah, you should be fine.")
    case "core i7":
        print ("Have fun!")
    case "core i9":
        print ("Our team designed nice loading screens")
    case _: 
        print ("Is that even a thing?")





# Short circuit (lazy evaluation) {minimal evaluation}
"""
When evaluating an expression that involves the or operator
Python can sometimes determine the result without evaluating 
all the operands. 
This is called short-circuit evaluation or lazy evaluation.
"""

is_admin = True
is_editor = False
can_edit = is_admin or is_editor

print(can_edit)
'''
M1_Task_09_StatementsInPython.py
Who has access
A
System properties
Type
Text
Size
2 KB
Storage used
2 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
28 Sept 2022 by Akash Chauhan
Opened
06:18 by me
Created
29 Sept 2022
No description
Viewers can download
from re import A, L
'''

x = int(input("Please enter an integer: "))

# If else statement
if x < 0:
    print('less than zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# For statements [The range() Function]
for i in range(1,5):
    print(i)

x = 5
# While loop statement [Values in reverse order]
while(x >= 1):
    print(x)
    x=x-1


# break and continue Statements, and else Clauses on Loops

n = 8
count  = 0
for x in range(2, n):
    if n % x == 0:
        print("Not a prime")
        count  = count+1
        break
    else:
        continue
if count == 0:
    print("It is a prime number")


# The pass statement does nothing. 
# It can be used when a statement is required syntactically 
# but the program requires no action.
def initlog():
    pass   # Remember to implement this!

initlog()

# while True:
#     pass





# match Statements
cpuModel = str.lower(input("Please enter your CPU model: "))
 
# The match statement evaluates the variable's value
match cpuModel:
    case "celeron": 
        print ("Forget about it and play Minesweeper instead...")
    case "core i3":
        print ("Good luck with that ;)")
    case "core i5":
        print ("Yeah, you should be fine.")
    case "core i7":
        print ("Have fun!")
    case "core i9":
        print ("Our team designed nice loading screens")
    case _: 
        print ("Is that even a thing?")





# Short circuit (lazy evaluation) {minimal evaluation}
"""
When evaluating an expression that involves the or operator
Python can sometimes determine the result without evaluating 
all the operands. 
This is called short-circuit evaluation or lazy evaluation.
"""

is_admin = True
is_editor = False
can_edit = is_admin or is_editor

print(can_edit)

'''
M2_Task_01_ListInPython.py
Who has access
A
System properties
Type
Text
Size
5 KB
Storage used
5 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
7 Oct 2022 by Akash Chauhan
Opened
06:19 by me
Created
8 Oct 2022
No description
Viewers can download
# 1. List

Data Structures: Lists
- Basic list operations
    - Creating a list
    - Inserting
    - Replacing
    - Removing an element
    - Searching
    - Sorting a list
- Methods of list objects
- Nested list
- Using lists as Stacks and Queues
- How efficient lists are when used as stack or queue 
'''

# 1. What is list in Python?
"""
- List is a Python’s in-built data structure
- Lists are muttable in nature, can be changed
- list can store different types of elements whereas array can 
  stores only single type of elements [int arr[3] = {1,2,3}; ]
- [], square brackets are used to create a list
"""

# 1.1 Empty list example
listSample = []
print(listSample)

# 2. Create a list!
Participants = ['John', 'Rakesh', 'Amit', 'Suresh', 123, 123.4, 'A']
print(Participants)

print (Participants[1])

print (Participants[-1])

print (Participants[-2])


# 3. Updating a list element
Participants[3]='Maria'
print (Participants)

# 4. Delete an element from the list
del Participants[2]
# del Participants[1:3]
print (Participants)
print (Participants[2])

# 5. Add new elements into a list
Participants.append("Akash")
Participants.append("123")
Participants.append(123)
Participants.append('A')
Participants.append(123.4)
print (Participants)

# 6. Replace Values in a List using indexing
l = [ 'Hardik','Rohit', 'Rahul', 'Virat', 'Pant']
l[0] = 'Akash'
print(l)

# 7. List Slicing
""""
list[index]
list[start,stop]
list[start,stop,step]
stop element would be excluded from the end result
"""
Participants = ['Suresh', 'John', 'Maria', 'Amit', 'Sumit', 'Cat', 123]

print(Participants)

print(Participants[1:3])

print(Participants[:2])

print(Participants[4:])

print(Participants[-2:])

print(Participants[-2::-1])

# 8. Find index of an element of the list
Maria_index = Participants.index("Maria")
print(Maria_index)

# ValueError: 'Maria123' is not in list
index = Participants.index("Maria123")
print(index)

# 9. Search an element in a list
x = [1,2,3,4,5]
print (2 in x)      #True
print (7 not in x)  #True

Participants = ['Suresh', 'John', 'Maria', 'Amit', 'Sumit', 'Cat', 123]


x = [1,2,3,4,5]
b = 7

# a = x.index(b)

if (b in x):
    a = x.index(b)
    print(a)
else:
    print("Element not found in the list!")


# 10. Sort a list
Participants.sort()
print(Participants)

# 10.1 Sort in reverse order
Participants.sort(reverse=True)
# The change will take place in the original string only, as 
# list is mutable in python
print(Participants) 

Numbers = [2,3,4,5,1]
Numbers.sort()
print(Numbers)

Numbers.sort(reverse = True)
print(Numbers)


# 11. Creating a list using range function
lst = range(1,9,2)
for i in lst:
  print(i)

# print(lst[0])

# 12. Concat two lists
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2
print(lst3)


# 13. Nested list as matrics [Nested list]
Participants = ['Suresh', 'John', 'Maria', 'Amit', 'Sumit', 'Cat', 123]
Newcomers = ['Joshua', 'Brittany']
# print(Newcomers)

print("__Bigger_List__")
Bigger_List = [Participants, Newcomers]

print(Bigger_List)
print(Bigger_List[0])
print(Bigger_List[1])

print(Bigger_List[0][4])
print(Bigger_List[1][1])

# print(Bigger_List[1][3])


# 14. Find max and min from a list
Numbers = [1,2,3,4,5]
print(max(Numbers))
print(min(Numbers))

# 15. Extra Methods of list Object
n = [1,2,3,4,5]
print(len(n))
n.append(6)
n.append(6)
print(n)

print(n.count(6))

# Element based
n.remove(6)
print(n)

# Index based
n.pop()
n.pop(0)

n.reverse()
print(n)

n.clear() # Delete all the elements and would leave an empty list at the end
print(n)


# 16. List comprehensions
"""List comprehensions represents creation of new lists 
from an iterable object like range, set, tuple and so on
"""
s = []
for i in range(1,9):
  s.append(i)

print(s)

lst = range(1,9,2)
for i in lst:
  print(i)

# yet to explore: set, tuple, dictionary -> list




#  tuple -> list
t = (1,2,3,4,5)
lst = list(t)
print(lst)

# list -> tuple
lst = [1,2,3,4,5]
t2 = (lst)
t3 = tuple(lst)
print(t2)
print(t3)


# 17. Using list as Stacks
# stack using list
"""LIFO order"""
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)
  
# Removes the last item
print(stack.pop()) 
print(stack)
  
# Removes the last item
print(stack.pop())
print(stack)

# 18. Using list as queue
# Initializing a queue
"""First in first out [FIFO]"""
queue = []

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# How efficient lists are when used as stack or queue
# As stack
"""
- The biggest issue is that it can run into speed issues as it grows.
- The items in the list are stored next to each other in memory,
- If the stack grows bigger than the block of memory that currently holds it
, then Python needs to do some memory allocations. This can lead to some 
append() calls taking much longer than other ones.
"""

# As Queue
"""
- However, lists are quite slow for this purpose 
because inserting or deleting an element at the beginning requires 
- shifting all of the other elements by one, requiring O(n) time.
"""
'''
M2_Task_02_SetTupleDictionaryInPython.py
Who has access
A
System properties
Type
Text
Size
4 KB
Storage used
4 KB
Location
Python Lab Elective
Owner
Akash Chauhan
Modified
7 Oct 2022 by Akash Chauhan
Opened
06:20 by me
Created
8 Oct 2022
No description
Viewers can download
'''
'''
1. Tuple
2. Sets
3. Difference between list and tuple 
4. Dictionary 
   - adding and removing keys
   - accessing values
   - Replacing values
   - Traversing Dictionaries
'''

# 2. Tuple in Python
'''
  - Unchangeable [Immutable]
  - Tuple items are ordered*
  - Allow duplicate values.
  - Use () to create tuple instead of []
'''

# Empty Tuple
t1 = ()

# Mutple types of data
t1 = (1,2,3,4,5, "AKash", 'A', 123.4)
print(t1)

t1 = 1,2,3,4,5,6,6




# Again tuple can store different types of elements
thistuple = ("apple", "banana", "cherry", "apple", 123, 123.4)
print(thistuple)

# Accessing the tuple elements
t1 = 1,2,3,4,5,6
print(t1[3])
print(t1[:])

# list -> tuple
lst = [1,2,3,4,5]
t2 = (lst)
print(t2)

t3 = tuple(lst)
print(t3)


# Functions to process tuple:
t1 = (1,2,3,4,5,6,6)

print(len(t1))
print(min(t1))
print(max(t1))
print(t1.count(6))
print(t1.index(2))
print(sorted(t1, reverse = True))
print(t1)

'''
We can not perform operations in tuples like: 
  - append() 
  - extend() 
  - insert()
  - clear() 
over tuple as tuples are immutable in python
'''

#3. Set 
'''
  - {} for set
  - Set is a collection which is unordered*
  - unchangeable [Immutable]
  - unindexed
  - No duplicate members
    [will automatically be deleted from the set]
'''
setV = {"apple", "banana", "cherry", "apple", 123, 123}
print(setV)

print("__SET__")
t1 = {2,1,3,4,5,6,6}

print(t1)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1, reverse = True))
print(t1)
#print(t1.count(6))
#print(t1.index(2))


'''
We can not perform these operations in sets like: 
  - append() 
  - extend() 
  - insert()
As sets immutable in python
'''

# 4. Dictonary
'''
- It is a key value pairs
- Dictonary is a collection which is ordered**
- changeable
- No duplicate members
'''

# Dictonary -> Operations
'''
4. Dictionary 
   - adding and removing keys
   - accessing values
   - Replacing values
   - Traversing Dictionaries
'''


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  123: 123.4,
  'A': 12
}

print(thisdict)

# Length of the dictionary
print(len(thisdict))

# Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  123: 12345,
  'A':123
}
print(thisdict["brand"])
print(thisdict[123])
print(thisdict['A'])


# Ordered or Unordered?
'''
- When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change
- Unordered means that the items does not have a defined order, you cannot refer to an item by using an index
- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered
'''

# Changeable or add a new element into a dictionary
'''Dictionaries are changeable, meaning that we can change
   add or remove items after the dictionary has been 
   created.
'''
# Dictionary Items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white" # new value
car["brand"] = "Ford123" # update value

x = car.keys()
print(x) #after the change

y = car.values()
print(y)


# Duplicates are, Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2021,
  "year": 2022,
  "year": 2023,
  "year": 2024,
  "year": 2025
}
print(thisdict)

# Get Keys and Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()

print(x,y)

# adding and removing keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# Removing keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()  # will remove the last item
print(thisdict)

# Traversing Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# Replacing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["brand"]= "Ford123"
print(thisdict)


letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

string_letters = str(letters)
lists_letters = list(letters)
tuples_letters = tuple(letters)
sets_letters = set(letters)


print("String: ", string_letters)
print() # for new line
print("Lists: ", lists_letters)
print() # for new line
print("Tuples: ", tuples_letters)
print() # for new line
print("Sets: ", sets_letters)