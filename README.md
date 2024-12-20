# Documentation for solving equation

Generating random equation, ask the user to answer the equation and display the result.

## User Manual

### Introduction

This Python program generates simple equations with random numbers and displays them using a graphical user interface (GUI) created with Tkinter. The user is prompted to solve the equations, and their answers are checked for correctness. The program keeps track of the user’s score and displays the total score at the end.

### System requirements

- Python 3.12
- Tkinter library (usually included with Python)
- generate_random_equation module (custom module for generating equations and checking answers)

### Installation and setup

1. Download Python: If you don’t have Python installed, download it from [official Python site](https://www.python.org/downloads/)
2. Install Tkinter: Tkinter is typically included with Python. If not, you can install it using the following command:
3. pip install tk
4. Install the generate_random_equation module if it’s not already available. This module should contain functions for generating random equations and checking answers.
5. Download the Program: Download the program files from the provided GitHub repository. (need to do this)
6. 
Running the Program
	Using Command Line:
1.	Save the provided code into a Python file, e.g., main_file_solve_equation.py.
2.	Open a terminal or command prompt.
3.	Navigate to the directory where the Python file is saved.
4.	Run the program by typing python main_file_solve_equation.py and pressing Enter.
Using an IDE:
1.	If you are using an IDE like PyCharm or VSCode, you can usually run the program by clicking a “Run” button.
Using the Program
1.	When the program starts, it will hide the main Tkinter window.
2.	The program will display a series of equations for you to solve. For example, you might see an equation like 3 * 𝑥 = 12.
3.	Enter your answer in the dialog box that appears and click OK.
4.	The program will inform you whether your answer is correct or incorrect.
5.	This process will repeat for a total of three equations.
6.	After all equations have been answered, the program will display your total score.
Example 
The program displays the equation as below:
 
1.	You enter 0.8 as the answer, the press OK button.
 
2.	The program informs you that your answer is correct.
 
If wrong, program informs you that your answer is wrong.
 
 
3.	This repeats for two more equations.
4.	Finally, the program displays your total score.
 
Technical Documentation
Code Overview
The program consists of the following main components:
•	Imports: Import necessary libraries and modules.
•	launch_quiz function: Main function to run the quiz.
•	Tkinter setup: Create and manage the Tkinter main window.
Detailed Code Explanation
Python 
'''
This Python program is to generates a simple equation with random numbers, such as (3 x 𝑥 = 12).
Displays the equation using GUI Tkinter.
Check if the user's answer id correct and display an appropriate message.
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


Functions and Modules
•	generate_random_equation module: Contains functions generate_equa and check_answer.
o	generate_equa(): Generates two random numbers for the equation.
o	check_answer(first_number, second_number, user_answer): Checks if the user’s answer is correct.
import random

# Function to generating equation from multiplication table, eg:3 × 𝑥 = 12
def generate_equa():
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    return first_number, second_number

# Function to check user answer against the correct answer
def check_answer(first_number, second_number, user_answer):
    correct_answer =  second_number / first_number
    format_user_answer = f"{user_answer:.1f}"
    format_correct_answer = f"{correct_answer:.1f}"
    return format_correct_answer == format_user_answer
    
Error Handling
•	The program includes error handling to manage invalid inputs and other exceptions, ensuring a smooth user experience.
GUI Elements
•	simpledialog.askfloat: Prompts the user to enter a floating-point number.
•	messagebox.showinfo: Displays messages to inform the user about the correctness of their answers and the final score.

