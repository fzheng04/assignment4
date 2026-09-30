import pytest
from app.calculation import Calculation
from app.calculation import CalculationFactory

def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(1, 2)


def test_calculation_attributes_and_execute():
    class TestCalculation(Calculation):
        def execute(self):
            return super().execute()

    calculation = TestCalculation(5, 3)

    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.execute() is None


def test_register_calculation():
    @CalculationFactory.register_calculation("test")
    class TestCalculation(Calculation):
        def execute(self):
            return self.a + self.b

    calculation = CalculationFactory.create("test", 2, 3)

    assert isinstance(calculation, TestCalculation)
    assert calculation.execute() == 5


def test_factory_invalid_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("invalid", 1, 2)