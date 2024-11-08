class CanNotAddTypesError(TypeError):
    """Raised when two types are added together, that are not compatible."""

    def __init__(self, self_type_descriptor: str, other_type_descriptor: str) -> None:
        super().__init__(f"Can not add {self_type_descriptor} to {other_type_descriptor}")
