from meeting3.geometry.exceptions import NonNumericInputException, NonPositiveInputException


def validate_side_format(side: str) -> float:
    """
    Checks whether the geometric figure side received as input is valid.
    Valid side should be a float positive number.

    If the side is valid, convert it to float and return.
    Otherwise, raise relevant exception:
    NonNumericInputException or NonPositiveInputException

    :param side: geometric side received as input
    """
    try:
        num = float(side)
        if num <= 0:
            raise NonPositiveInputException(f"Input {num} is not positive number")
        return num
    except ValueError:
        raise NonNumericInputException(f"Input {side} is not a number")
