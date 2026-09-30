from app.calculation import CalculationFactory


class Calculator:
    history = []

    @staticmethod
    def calculate(operation: str, a: float, b: float) -> float:
        calculation = CalculationFactory.create(operation, a, b)
        result = calculation.execute()

        Calculator.history.append(
            {
                "operation": operation,
                "a": a,
                "b": b,
                "result": result,
            }
        )

        return result

    @staticmethod
    def get_history():
        return Calculator.history

    @staticmethod
    def clear_history():
        Calculator.history.clear()


def calculator():
    """REPL calculator."""

    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        user_input = input(
            "Enter an operation (add, subtract, multiply, divide, power) "
            "and two numbers, or 'exit' to quit: "
        )

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        try:
            operation, num1, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print(
                "Invalid input. Please follow the format: "
                "<operation> <num1> <num2>"
            )
            continue

        try:
            result = Calculator.calculate(operation, num1, num2)
        except ValueError as e:
            print(e)
            continue

        print(f"Result: {result}")