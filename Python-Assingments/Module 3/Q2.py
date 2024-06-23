#How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
'''To remove the last object from a list, you can use the pop() function in Python.
This function removes the item at the specified position in the list, and returns it.
If no index is specified, pop() removes and returns the last item in the list.

Suppose we have a list called list1:

list1 = [2, 33, 222, 14, 25]
To remove the last object from this list, we can call list1.pop() without any arguments:

last_obj = list1.pop()
Now last_obj contains the last object in the list (in this case, 25), and list1 is:

[2, 33, 222, 14]
