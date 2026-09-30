import pytest
from app.calculation import Calculation


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