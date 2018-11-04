a = "Hello, World!"
print(a[1])

#1st character of string, similar to list

b = "Hello, World!"
print(b[2:5])

#2nd to 5th (not including 5th), similar to list

a.upper() 
#HELLO, WORLD
a.lower()
#hello, world

#---------------------------------------------------------------------------------------------

name = "bob"

'Hello, {}'.format(name)
# Hello, bob
#New style of string formatting, preferred over %s

#Default substitutes based on order

'{}, {}'.format("Hello", "World")
# Hello, World
'{}, {}'.format("World", "Hello")

#Substitutions can be named

'{h}, {w}'.format(h="Hello", w="World")
'{h}, {w}'.format(w="World", h="Hello")
#Both result in "Hello, World"

#---------------------------------------------------------------------------------------------

#f-strings
#Are interpreted, can have subsitutions and math
a = "Hello"
b = "World"

f'{a}, {b}'
f'{2 * 3}'

c= 10
f'2 times {c} is {2 * c}'