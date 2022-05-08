class GeometryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NonNumericInputException(GeometryException):
    pass


class NonPositiveInputException(GeometryException):
    pass


class InvalidTriangleException(GeometryException):
    pass