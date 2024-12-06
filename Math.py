import random

def generate_question():
    """Generate a random arithmetic question with a word problem and simple equation."""
    operations = ['+', '-', '*', '/']
    operator = random.choice(operations)
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    if operator == '+':
        question = f"John has {number1} apples. He found {number2} more apples. How many apples does John have now?"
    elif operator == '-':
        if number2 > number1:
            number1, number2 = number2, number1  # Swap numbers to ensure a positive result
        question = f"Sara had {number1} cookies. She ate {number2} cookies. How many cookies does Sara have left?"
    elif operator == '*':
        question = f"Lisa has {number1} baskets and each basket contains {number2} apples. How many apples does she have in total?"
    elif operator == '/':
        divisible_numbers = [num for num in range(1, number1 + 1) if number1 % num == 0]
        number2 = random.choice(divisible_numbers)
        question = f"Emily has {number1} candies and she wants to distribute them equally among {number2} friends. How many candies will each friend get?"

    equation = f"{number1} {operator} {number2}"
    return question, equation

def check_answer(equation, user_answer):
    """Check if the user's answer to the equation is correct."""
    correct_answer = eval(equation)
    return int(user_answer) == correct_answer, correct_answer

def play_game():
    """Main function to play the math game."""
    score = 0
    num_questions = 5

    print("Welcome to the Math Game!")
    print("Solve the following word problems and equations:")

    for _ in range(num_questions):
        question, equation = generate_question()
        print(question)
        user_answer = input("Your answer: ")
        
        is_correct, correct_answer = check_answer(equation, user_answer)
        
        if is_correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.\n")

    print(f"Game Over! Your final score is {score}/{num_questions}.")

play_game()
