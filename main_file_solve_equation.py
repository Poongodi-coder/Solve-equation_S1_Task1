'''
This Python program is to generates a simple equation with random numbers, such as (3 x 𝑥 = 12).
Displays the equation using GUI Tkinter.
Check if the user's answer correct and display an appropriate message.
Repeat the process for several equations, keeping track of the user's score.
After all equation questions have been answered, output the total score.
'''

import random
import generate_random_equation as gre
import tkinter as tk
from tkinter import simpledialog, messagebox

def launch_quiz():
    score = 0
    num_question = 3

    #Using for loop to generate random equation
    for iteration in range(num_question):
        # Call and store the two randomly generated numbers in the variables
        first_number, second_number = gre.generate_equa()
    
        # Display the equation to the user to answer
        equation = f"{first_number} * 𝑥 = {second_number}"


        # Catching exceptions
        try:
            # Get the answer from the user.
            user_answer = simpledialog.askfloat("Solve", equation)
        except ValueError:
            messagebox.showinfo("Invalid input. Please enter a valid numbers.")
            user_answer = simpledialog.askfloat("Solve", equation)
        except Exception as e:
            messagebox.showinfo("An error occurred: {e}. Please enter a valid number")

        # Call the function to check user answer against correct answer and store the boolean value.
        iscorrect = gre.check_answer(first_number, second_number, user_answer)

        # Decide whether the user answer is correct or not and display the message accordingly.
        if iscorrect == True:
            messagebox.showinfo("Result", "Your answer is correct, well done.")
            score += 1
        else:
            messagebox.showinfo("Result", "Your answer is wrong, better luck next time.")

    # Total score in message box
    messagebox.showinfo("Final score:", f"Your total score is {str(score)}/{str(num_question)}")
    return score, num_question

# Create the main window
root = tk.Tk()
# Hide the main window
root.withdraw()

# Call the function to launch quiz and store the return values.
launch_quiz()

# Destroy the root window
root.destroy()