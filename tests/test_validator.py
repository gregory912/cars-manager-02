from car.validator import *


def test_validate_model():
    """
    Test if the validate_model method validates the entered data correctly
    """
    assert validate_model("AUDI")
    assert not validate_model("aAUDI")
    assert not validate_model("AUDI ")
    assert not validate_model(" AUDI")
    assert not validate_model("AUDI1")
    assert not validate_model("")
    assert not validate_model(" ")


def test_validate_price_mileage():
    """
    Test if the validate_price_mileage method correctly validates the entered data
    """
    assert validate_price_mileage(0)
    assert validate_price_mileage(100)
    assert not validate_price_mileage(-100)
    assert validate_price_mileage(Decimal(100))
    assert not validate_price_mileage(Decimal(-100))


def test_validate_components():
    """
    Test if the validate components method validates the entered data correctly
    """
    assert validate_components("ABS")
    assert validate_components("ROOF RACK")
    assert validate_components("ROOF   RACK")
    assert not validate_components("aABS")
    assert not validate_components(" ABS")
    assert not validate_components("ABS ")
    assert not validate_components(" ABS ")
    assert not validate_components("ABS1")
    assert not validate_components("ABS1")
    assert not validate_components("")
    assert not validate_components(" ")
