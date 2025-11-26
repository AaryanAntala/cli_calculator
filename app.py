import sys
import argparse
from typing import Union


def add(x: float, y: float) -> float:   
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def power(x: float, y: float) -> float:
    return x ** y


def modulo(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot calculate modulo with zero divisor")
    return x % y


# Operation mapping
OPERATIONS = {
    'add': (add, '+'),
    'sub': (subtract, '-'),
    'mul': (multiply, '*'),
    'div': (divide, '/'),
    'pow': (power, '**'),
    'mod': (modulo, '%')
}


def get_number_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye!")
            sys.exit(0)


def interactive_mode():
    """Run calculator in interactive mode with menu."""
    print("\n" + "="*50)
    print("CLI CALCULATOR - Interactive Mode")
    print("="*50)
    
    while True:
        print("\nAvailable Operations:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Power          (**)")
        print("  6. Modulo         (%)")
        print("  0. Exit")
        
        try:
            choice = input("\nSelect operation (0-6): ").strip()
            
            if choice == '0':
                print("\nThank you for using CLI Calculator!")
                break
            
            # Map choice to operation
            operation_map = {
                '1': 'add',
                '2': 'sub',
                '3': 'mul',
                '4': 'div',
                '5': 'pow',
                '6': 'mod'
            }
            
            if choice not in operation_map:
                print("Invalid choice. Please select 0-6.")
                continue
            
            operation = operation_map[choice]
            func, symbol = OPERATIONS[operation]
            
            # Get numbers
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            
            # Perform calculation
            try:
                result = func(num1, num2)
                print(f"\nResult: {num1} {symbol} {num2} = {result}")
            except ValueError as e:
                print(f"\nError: {e}")
                
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye!")
            break


def command_line_mode(operation: str, num1: float, num2: float):

    if operation not in OPERATIONS:
        print(f"Error: Unknown operation '{operation}'")
        print(f"Available operations: {', '.join(OPERATIONS.keys())}")
        sys.exit(1)
    
    func, symbol = OPERATIONS[operation]
    
    try:
        result = func(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """Main entry point for the calculator application."""
    parser = argparse.ArgumentParser(
        description='CLI Calculator - Perform arithmetic operations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py add 5 3          # Addition: 5 + 3
  python app.py sub 10 4         # Subtraction: 10 - 4
  python app.py mul 6 7          # Multiplication: 6 * 7
  python app.py div 20 4         # Division: 20 / 4
  python app.py pow 2 8          # Power: 2 ** 8
  python app.py mod 17 5         # Modulo: 17 % 5
  python app.py                  # Interactive mode
        """
    )
    
    parser.add_argument(
        'operation',
        nargs='?',
        choices=list(OPERATIONS.keys()),
        help='Operation to perform'
    )
    parser.add_argument(
        'num1',
        nargs='?',
        type=float,
        help='First number'
    )
    parser.add_argument(
        'num2',
        nargs='?',
        type=float,
        help='Second number'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='CLI Calculator v1.0.0'
    )
    
    args = parser.parse_args()
    
    # Interactive mode if no arguments provided
    if args.operation is None:
        interactive_mode()
    elif args.num1 is None or args.num2 is None:
        print("Error: Please provide both numbers for the operation")
        parser.print_help()
        sys.exit(1)
    else:
        command_line_mode(args.operation, args.num1, args.num2)


if __name__ == "__main__":
    main()