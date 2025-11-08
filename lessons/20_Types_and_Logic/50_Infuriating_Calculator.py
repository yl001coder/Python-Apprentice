"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""
from tkinter import simpledialog, messagebox, Tk
# Import the required modules
window = Tk()
window.withdraw()
# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
num1 = simpledialog.askfloat("Infuriating Calculator", "What is your first number?")

# Ask the user for the second number
num2 = simpledialog.askfloat("Infuriating Calculator", "What is your second number?")

# Ask the user for the math operation
operation = simpledialog.askstring("Infuriating Calculator", "What is the operation [string only]")
if(operation == "addition"):
    messagebox.showinfo("Your Answer")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open