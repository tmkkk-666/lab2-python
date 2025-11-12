import time
from functools import wraps
import os
import random

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' execution time: {execution_time:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def sum_two_numbers(a, b):
    result = a + b
    print(f"Calculation result: {a} + {b} = {result}")
    return result

@timer_decorator
def read_and_write_file():
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    output_path = os.path.join(script_dir, 'output.txt')

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            tokens = f.read().strip().split()
        
        # Convert to float numbers
        numbers = [float(token) for token in tokens]
        
        # Check if at least two numbers exist
        if len(numbers) < 2:
            raise ValueError(f"Not enough numbers in file (total: {len(numbers)})")
        
        # Randomly select two different numbers
        a, b = random.sample(numbers, 2)

        result = a + b

        # Write to output.txt
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"All numbers in file: {numbers}\n")
            f.write(f"Randomly selected two numbers: {a}, {b}\n")
            f.write(f"Calculation result: {a} + {b} = {result}\n")

        print(f"Successfully selected {a} and {b} from {len(numbers)} numbers")
        print(f"Result written to output.txt")
        return result

    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

def main():
    print("Test function 1: Calculate sum of two numbers")
    sum_two_numbers(1, 2)

    print("\nTest function 2: Read from file and write result")
    read_and_write_file()

if __name__ == "__main__":
    main()