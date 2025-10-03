# File: arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation between two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation or an error message if division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        # Optional: handle invalid operation input, though main.py is assumed to provide valid input
        return f"Error: Invalid operation '{operation}'"

if __name__ == '__main__':
    # Example tests for the function
    print("Testing perform_operation:")
    
    # Addition
    print(f"5 + 6 = {perform_operation(5, 6, 'add')}") # Expected: 11.0
    
    # Subtraction
    print(f"10 - 3.5 = {perform_operation(10, 3.5, 'subtract')}") # Expected: 6.5
    
    # Multiplication
    print(f"4 * 7 = {perform_operation(4, 7, 'multiply')}") # Expected: 28.0
    
    # Division
    print(f"10 / 2 = {perform_operation(10, 2, 'divide')}") # Expected: 5.0
    
    # Division by Zero Handling
    print(f"8 / 0 = {perform_operation(8, 0, 'divide')}") # Expected: Error: Cannot divide by zero
