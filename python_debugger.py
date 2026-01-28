'''
Command	LongForm	What it does in your code
n	    next	    Moves to the next line: z = add(x, y). It won't go inside the function; it just finishes it and moves to the print statement.
s	    step	    Steps into the add function. Use this if you suspect the bug is inside the math logic itself.
c	    continue	Stops debugging and runs the rest of the script normally until it finishes or hits another breakpoint.
r	    return	    If you are inside add(), this finishes the function and returns you to the caller (z = add...).
'''

'''

Command	    What it does in your code
l       	Shows a "snippet" of the code (usually 11 lines) around where you are currently paused.
p x	        Prints the value of the variable x. In your case, it would output 10.

'''

import pdb
breakpoint()

def add(x, y):
    print("Inside add function")
    return x + y

x = 10
y = 20
z = add(x, y)
print(f"The sum of {x} and {y} is {z}") 