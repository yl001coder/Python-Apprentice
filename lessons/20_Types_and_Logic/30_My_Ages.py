"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")

Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")
"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

age = simpledialog.askinteger("Your Age", "How old are you?")
if(age == 11):
    messagebox.showinfo('What you are', "You are awesome!")
elif(age < 3 & age > -1):
    messagebox.showinfo('What you are', "A baby. How are you even using this?")
elif(age > 2 & age < 6):
    messagebox.showinfo('What you are', "A toddler. A pretty smart one at that.")
elif(age != 11 & age > 5 & age < 13):
    messagebox.showinfo('What you are', "A child. Nice.")
elif(age > 12 & age < 20):
    messagebox.showinfo('What you are', "Teenager. Intresting.")
elif(age > 19 & age < 65):
    messagebox.showinfo('What you are', "An adult. Are you seriously going to be on here? Get a life.")
elif(age > 64):
    messagebox.showinfo('What you are', "A senior citizen. Must get all those benefits huh?")
# Ask the user's age

# Use if statements to determine the age group
# and create a message

# Show the message to the user

window.mainloop()  # Keeps the window open

# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.