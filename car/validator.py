from decimal import Decimal


def validate_model(model: str) -> bool:
    """
    Validate a model that can only have uppercase letters
    """
    return True if model.isupper() and model.isalpha() else False


def validate_price_mileage(value: Decimal | int) -> bool:
    """
    Validate the price and mileage that cannot be less than 0
    """
    return True if value >= 0 else False


def validate_components(text: str) -> bool:
    """
    Validate components that can only contain uppercase and white space
    """
    if not text:
        return False
    if text[:1] == ' ' or text[-1:] == ' ':
        return False
    if not text.replace(' ', '').isupper():
        return False
    for x in text:
        if not (x == ' ' or x.isalpha()):
            return False
    return True
