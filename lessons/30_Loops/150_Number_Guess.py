""" 
Number Guess Game

Pick a random number between 1 and 100. If the random number is divisible by 7,
pick another number and continue picking new numbers until the random number is
not divisible by 7. ( hint: use a loop! )

Ask the user to guess the number. If the user's guess is higher than the random
number, tell the user the guess is too high. If the user's guess is lower than
the random number, tell the user the guess is too low. If the user guesses the
number, tell the user the guess is correct and stop the game. If the user does
not guess the number, allow the user to keep guessing until the user gets the
right answer.


Write the main part of your program as a loop. If the user guesses the number,
break out of the loop. If the user does not guess the number, continue the loop.

If the user guesses a number that is divisible by 7, tell the user "that is a
very bad number, starting over " and pick another number and continue picking
new numbers until the number is not divisible by 7.

Get a random number:
    n = random.randint(1, 100)

Use the ask_integer function to get the user's guess, like this:
    guess = ask_integer("Guess a number between 1 and 100: ")

Note: The prompts and output for your program will be in the teminal
at the bottom of the editor screen; this program does not use the GUI.
"""

import random
from tkinter import simpledialog, messagebox, Tk

def ask_integer(prompt):
    """Function to ask the user for an integer"""
    simpledialog.askstring('Question Box', prompt)
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

# Pick the random number
game = True
n = random.randint(1,100)
while game == True:
    print("ran") 
    print("""I grew up in the Roxbury slums
          with my mom and a series of bums
          guys who showed me all the ways a man could fail
          got through law school by busting my 
          worked two jobs in addition to class
          so forgive me for not weeping at your tale
          
          there's a chip on my shoulder
          it's a big as a boulder
          with the chance i've been given
          i've gotta be 
          driven as hell
          i'm so close i can taste it
          and i'm not gonna waste it
          i've got a chip on my shoulder
          you might wanna get one as well
          
          well, i don't go to parties a lot
          not good use of the itme that i've got
          can't spend hours doing my hair and staying in shape
          (i don't spend hours!)
          but i know it'll all be worthwhile
          when i win my first lucrative trial
          and buy my mom that great big house out on the cape
          aw, that's sweet
          no, that's the chip on my shoulder
          i hugged my mom and told her
          with the chance i've been given
          i'm gonna be driven as hellThough I can't take the day off
        I just think of the payoff
        You need a chip on your shoulder  
        Little Miss Woods comma Elle
        I just need to prove to everyone that I'm serious
        What you need is to get to work
        Where are your law books?
        Um, well, I know they're here somewhere
        You know, this vanity's real picturesque
        But it started its life as a desk
        Clear it off and find some room for books instead
        What are you doing?
        Can you live without this?
        Can you live without that?
        I don't know what this is
    It's for hair
    Wear a hat
    Spend some time improving what's inside your head
    Out, out, put it in storage
    Sell it on eBay, leave it behind
    Out, out, what, are you angry?
    Good, so get angry, you may find
    The chip on your shoulder (ugh!)
    Ooh, the room just got colder (hey!)
    But with the chance you've been given
    Why are you not driven as hell?
    There's just no way around it
    You've gotta plough through 'til you-
    Found it!
    Been reading it hard, I can tell
    Bye, Warner!
    Have a great Thanksgiving! 
    Say hi to your Mom and Dad for me
    And Grandma Bootsie

+Define malum prohibitum
Malum prohibitum is, um
An act prohib-
An act prohibited by law
Like jaywalking or chewing gum in Singapore
Therefore, malum in se
Is an action, that's evil in itself
Assault, murder, white shoes after Labor Day
Good
Where are you going?
Home, of course
It's Thanksgiving break, remember?
Interesting
What?
Well, I predict you will probably pass (yes!)
In the bottom percent of your class (what?)
If you're going for mediocre, you've done great
That's not fair
Look, they laughed at me, like they're laughing at you
We can't win if we don't follow through
Might I venture your vacation plans can wait?
Why do you always have to be right?
Bye, Warner!
Merry Christmas!
Enjoy Vale!
Ho, ho, ho!
Emmett!
For you
Not as good as going home for Christmas, but
You are too sweet
It's a real time saver
Shampoo and conditioner in one
Thank you, you are so adorable to think of me
Elle, hey!
Warner!
Have you seen Vivienne? I've been looking for her everywhere
Yeah, I mean, no
Great, we're gonna miss our flight
Um, Elle?
I don't know if you've noticed before
But each time Warner walks through the door
Your IQ goes down to 40, maybe less (huh?)
Though it's hardly my business to say
Could it be the real thing in your way
Is the very guy you're trying to impress?
Yes!
I've been smiling and sweet
And thoroughly beaten, blowing my chance
Let's not chase him away
Let's face him and say, "hey, punk, let's dance!"
This chip on my shoulder
Makes me smarter and bolder
No more whining or blaming
I am reclaiming my pride
Grab that book and let's do this
Instead of doodling hearts all through this
Now, there's a chip on my shoulder (chip on my shoulder)
Let's see him knock it aside (ah)
Mr. Latimer was clearly within his rights to ask for visitation
Without his sperm, the child in question wouldn't exist
Now you're thinking like a lawyer
Yes, Ms. Woods?
Mr. Huntington makes an excellent point
But, did the defendant keep a log
Of every sperm emission made throughout his life?
Interesting, why do you ask?
Well, unless the defendant attempted to contact every sexual encounter
To find if a child resulted from those unions
He has no parental claim over this child whatsoever
Why now? Why this sperm?
I see your point
And, by Mr. Huntington's standard
All masturbatory emissions where the sperm was clearly
Not seeking an egg could be called reckless abandonment
Ms. Woods, you just won your case
Omigod (wait, hold on, we just won the case)
Omigod (Elle got all up in Warner's face)
Omigod (I am starting to like this place)
Omig-
Ms. Woods, excellent work today
I assume you're applying for my internship
Do you have a resumé?
I'm one step ahead of you
Here you go, and thanks in advance for your consideration
Dear God, it's scented
Three months ago, I would've recycled this
Make sure to put it on file
Guess she got a chip on her shoulder
Maybe some wise man told her
With the chance we've been given
We've gotta be driven as hell!
She was something to see there
I'm just happy I could be there!
First big test and she aced it
She's so close, she can taste it!
She got a chip on her shoulder
Guess you never can tell
With little Miss Woods comma Elle!
No, you never can tell (Elle Woods, woods comma Elle)
With little Miss Woods comma Elle
""")
    ip = simpledialog.askstring("What is your number?")
    if(ip == n):
        ask_integer("what is your number")
        messagebox.showinfo("question box", "Yay! You guess correctly!")
    elif(ip > n):
        messagebox.showinfo("question box","your number is too high")
    elif(ip < n):
        messagebox.showinfo("question box","your number is too low")
    elif(ip%7 == 0):
        messagebox.showinfo("question box","start over!")


# In your loop:

    # Get the user's guess

    # If the user's guess is divisible by 7, tell the user to start over

    # If the user's guess is too high, tell the user

    # If the user's guess is too low, tell the user
    
    # If the user's guess is correct, tell the user and break out of the loop