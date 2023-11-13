import random

def generate_random_integer(minimum, maximum):
    """
    Generates a random integer between the specified minimum and maximum values.
    
    Args:
        minimum (int): The minimum value of the random integer.
        maximum (int): The maximum value of the random integer.
    
    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(minimum, maximum)

def choose_random_operator():
    """
    Chooses a random arithmetic operator from the set {+, -, *}.
    
    Returns:
        str: A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def perform_operation(number1, number2, operator):
    """
    Performs the arithmetic operation based on the provided numbers and operator.
    
    Args:
        number1 (int): The first operand.
        number2 (int): The second operand.
        operator (str): The arithmetic operator.
    
    Returns:
        tuple: A tuple containing the problem expression and the correct answer.
    """
    problem_expression = f"{number1} {operator} {number2}"

    try:
        if operator == '+':
            correct_answer = number1 + number2
        elif operator == '-':
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2
    except Exception as e:
        print(f"Error performing the operation: {e}")
        return None, None

    return problem_expression, correct_answer

def math_quiz():
    """
    Conducts a math quiz game with the user.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = choose_random_operator()

        problem, answer = perform_operation(number1, number2, operator)

        if problem is None:
            continue  # Skip to the next iteration if an error occurred

        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Skip to the next iteration if input is not a valid integer

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
