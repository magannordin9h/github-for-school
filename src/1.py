import random
def get_random_python_code():
    # Create a list of possible function names
    function_names = ['add', 'subtract', 'multiply', 'divide']
    
    # Pick a random function name from the list
    function_name = random.choice(function_names)
    
    # Create a list of possible operands (numbers)
    operands = [1, 2, 3, 4, 5]
    
    # Pick two random operands from the list
    op1 = random.choice(operands)
    op2 = random.choice(operands)
    
    # Use the picked function name and operands to create a valid Python expression
    expression = f"{function_name}({op1}, {op2})"
    
    return expression