from car.validator import *


def test_validate_model_correct_value():
    """
    Check that the validate_model method returns True for a valid item
    """
    assert validate_model("AUDI")


def test_validate_model_lower_letter():
    """
    Test that the validate_model method returns False for the lowercase element
    """
    assert not validate_model("aAUDI")


def test_validate_model_space():
    """
    Test that the validate_model method returns False for the element with a space
    """
    assert not validate_model("AUDI ")
    assert not validate_model(" AUDI")


def test_validate_model_digit():
    """
    Test that the validate_model method returns False for the item with numbers
    """
    assert not validate_model("AUDI1")


def test_validate_model_empty_string():
    """
    Test that the validate_model method returns False for the empty string
    """
    assert not validate_model("")


def test_validate_model_empty_space():
    """
    Test that the validate_model method returns False for a blank space
    """
    assert not validate_model(" ")


def test_validate_price_mileage_correct_values():
    """
    Test that the validate_price_mileage method returns True for valid values
    """
    assert validate_greater_than_0(0)
    assert validate_greater_than_0(100)


def test_validate_price_mileage_correct_values_decimal():
    """
    Test that the validate_price_mileage method returns True for valid values
    """
    assert validate_greater_than_0(Decimal(100))


def test_validate_price_mileage_wrong_value():
    """
    Test that the validate_price_mileage method returns False for negative values
    """
    assert not validate_greater_than_0(-100)


def test_validate_price_mileage_wrong_value_decimal():
    """
    Test that the validate_price_mileage method returns False for negative values
    """
    assert not validate_greater_than_0(Decimal(-100))


def test_validate_components_single_word_component():
    """
    Test that the validate_components method returns True for valid values
    """
    assert validate_components("ABS")


def test_validate_components_many_words_component():
    """
    Test that the validate_components method returns True for valid values
    """
    assert validate_components("ROOF RACK")
    assert validate_components("ROOF   RACK")


def test_validate_components_lower_letter():
    """
    Test that the validate_components method returns False for lowercase elements
    """
    assert not validate_components("aABS")


def test_validate_components_space():
    """
    Test that the validate_components method returns False for items with a space
    """
    assert not validate_components(" ABS")
    assert not validate_components("ABS ")
    assert not validate_components(" ABS ")


def test_validate_components_digits():
    """
    Test that the validate_components method returns False for items with numbers
    """
    assert not validate_components("ABS1")
    assert not validate_components("ABS1")


def test_validate_components_empty_string():
    """
    Test that the validate_components method returns False for an empty string
    """
    assert not validate_components("")


def test_validate_components_empty_space():
    """
    Test that the validate_components method returns False for a blank space
    """
    assert not validate_components(" ")
