class CanNotAddTypesError(TypeError):
    """Raised when two uncompatible quantities are added to one another."""

    def __init__(self, self_type_descriptor: str, other_type_descriptor: str) -> None:
        super().__init__(f"Can not add {other_type_descriptor} to {self_type_descriptor}")


class CanNotSubtractTypesError(TypeError):
    """Raised when two uncompatible quantities are subtracted from one another."""

    def __init__(self, self_type_descriptor: str, other_type_descriptor: str) -> None:
        super().__init__(f"Can not subtract {other_type_descriptor} from {self_type_descriptor}")


class NoUnitSpecifiedError(TypeError):
    """Raised when a Vector[_QuantityBase] is converted to a np.array without specifying a unit."""

    def __init__(self) -> None:
        super().__init__(
            "When a vector with quantity elements is converted into a numpy array, a unit must be "
            "specified."
        )
