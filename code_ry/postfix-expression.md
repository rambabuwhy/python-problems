# postfix expression

In this example, the postfix expression "53\*2+" would be evaluated as follows:

* Push 5 to the stack
* Push 3 to the stack
* Encounter '\*', pop 3 and 5, calculate 3 \* 5, push 15 to the stack
* Push 2 to the stack
* Encounter '+', pop 2 and 15, calculate 2 + 15, push 17 to the stack

```python

def evaluate_postfix(expression):
    # Initialize an empty stack to store operands
    stack = []

    # Define a set of valid operators
    operators = set(['+', '-', '*', '/', '**'])

    # Split the expression into tokens
    tokens = expression.split()

    try:
        # Iterate through each token in the expression
        for token in tokens:
            # Check if the token is a digit or a negative number
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(float(token))  # Push operands to the stack
            elif token in operators:
                if token == '**':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 ** operand2
                    stack.append(result)  # Push the result of the power operation to the stack
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()

                    # Perform the corresponding arithmetic operation based on the operator
                    if token == '+':
                        result = operand1 + operand2
                    elif token == '-':
                        result = operand1 - operand2
                    elif token == '*':
                        result = operand1 * operand2
                    elif token == '/':
                        result = operand1 / operand2

                    stack.append(result)  # Push the result to the stack
            else:
                raise ValueError("Invalid token in the expression")

    except (IndexError, ValueError):
        print("Error: Malformed postfix expression")

    # Check if the expression is well-formed and return the result
    if len(stack) == 1:
        return stack[0]
    else:
        print("Error: Malformed postfix expression")

# Example usage:
postfix_expression = "2 3 **"
result = evaluate_postfix(postfix_expression)
if result is not None:
    print(f"The result of the postfix expression {postfix_expression} is: {result}")

```
