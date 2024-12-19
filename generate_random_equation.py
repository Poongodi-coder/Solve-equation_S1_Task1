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