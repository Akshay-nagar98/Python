#Differentiate between append () and extend () methods?
'''
The append() method in Python adds a single element to an existing list as a single item at the end of the list.
It does not return a new list but updates the original list by adding the specified element. The list’s length increases by one.

Syntax:
list.append(item)

The extend() method in Python adds multiple elements from an iterable (like another list or tuple) at once to an existing list by adding each element from the iterable individually to the end of the initial list.
It alters the initial list directly without returning any value.When you extend a string using extend(), it appends each character as you iterate over it since strings are iterable objects in Python.

lista = [1, 2] b=[3,4] lista.extend(b)
'''
