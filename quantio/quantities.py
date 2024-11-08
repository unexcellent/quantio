class Length:
    """The one-dimensional extent of an object or the distance between two points."""

    _meters: float

    def __init__(self, meters: float = 0.0) -> None:
        """Construct this class with the used units."""
        self._meters = meters

    @property
    def meters(self) -> float:
        """The length in meters."""
        return self._meters
