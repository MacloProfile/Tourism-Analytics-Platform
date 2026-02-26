from decimal import Decimal


def safe_float(value):
    if value is None:
        return None

    if isinstance(value, Decimal):
        if value.is_nan():
            return None
        return float(value)

    if isinstance(value, float) and value != value:
        return None

    return float(value)
