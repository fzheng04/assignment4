from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        pass

class CalculationFactory:
    _calculations = {}

    @classmethod
    def register_calculation(cls, name):
        def decorator(calculation_class):
            cls._calculations[name] = calculation_class
            return calculation_class
        return decorator

    @classmethod
    def create(cls, operation: str, a: float, b: float):
        if operation not in cls._calculations:
            raise ValueError(f"Unknown operation: {operation}")

        calculation_class = cls._calculations[operation]
        return calculation_class(a, b)