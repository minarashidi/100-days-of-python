from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# using recursion to start a new calculation
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        operation = operations[operation_symbol]
        result = operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        calculate_continue = input(
            "type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if calculate_continue == "y":
            num1 = result
        else:
            should_continue = False
            calculator()


# calculator()


def calculator_higher_order_function(a, b, fun):
    return fun(a, b)


print(calculator_higher_order_function(2, 3, add))
print(calculator_higher_order_function(2, 3, multiply))
