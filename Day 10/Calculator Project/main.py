import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    should_continue = True
    n1 = float(input("type first number: "))
    while should_continue:
        operation = input("type mathematical operator: ")
        n2 = float(input("type next number: "))
        result = operations[operation](n1, n2)
        print(f"The result of {n1} {operation} {n2} is: {result}")
        n1 = result
        should_continue = input("Do you want to continue working with the previous result? ").lower()
        if should_continue == "no":
            should_continue = False


if __name__ == '__main__':
    print(art.logo)
    while True:
        calculator()