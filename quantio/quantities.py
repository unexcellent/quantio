from __future__ import annotations

from ._quantity_base import _QuantityBase


class Acceleration(_QuantityBase):
    """Rate of change of velocity."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        meters_per_square_second: float = 0.0,
        g_force: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += meters_per_square_second * 1
        self._base_value += g_force * (1 / 9.8)

    @property
    def meters_per_square_second(self) -> float:
        """The acceleration in meters per square second."""
        return self._base_value / 1

    @property
    def g_force(self) -> float:
        """The acceleration in g force."""
        return self._base_value / (1 / 9.8)

    # --- End of auto generated part. ---


class Angle(_QuantityBase):
    """The figure formed by two rays."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        degrees: float = 0.0,
        radians: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += degrees * (3.141592653589793 / 180)
        self._base_value += radians * 1

    @property
    def degrees(self) -> float:
        """The angle in degrees."""
        return self._base_value / (3.141592653589793 / 180)

    @property
    def radians(self) -> float:
        """The angle in radians."""
        return self._base_value / 1

    # --- End of auto generated part. ---


class Area(_QuantityBase):
    """The two-dimensional extent of an object."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        square_miles: float = 0.0,
        square_kilometers: float = 0.0,
        square_meters: float = 0.0,
        square_feet: float = 0.0,
        square_inches: float = 0.0,
        square_centimeters: float = 0.0,
        square_millimeters: float = 0.0,
        square_micrometers: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += square_miles * 1609.34**2
        self._base_value += square_kilometers * 10 ** (3 * 2)
        self._base_value += square_meters * 1
        self._base_value += square_feet * 0.3048**2
        self._base_value += square_inches * 0.0254**2
        self._base_value += square_centimeters * 10 ** (-2 * 2)
        self._base_value += square_millimeters * 10 ** (-3 * 2)
        self._base_value += square_micrometers * 10 ** (-6 * 2)

    @property
    def square_miles(self) -> float:
        """The area in square miles."""
        return self._base_value / 1609.34**2

    @property
    def square_kilometers(self) -> float:
        """The area in square kilometers."""
        return self._base_value / 10 ** (3 * 2)

    @property
    def square_meters(self) -> float:
        """The area in square meters."""
        return self._base_value / 1

    @property
    def square_feet(self) -> float:
        """The area in square feet."""
        return self._base_value / 0.3048**2

    @property
    def square_inches(self) -> float:
        """The area in square inches."""
        return self._base_value / 0.0254**2

    @property
    def square_centimeters(self) -> float:
        """The area in square centimeters."""
        return self._base_value / 10 ** (-2 * 2)

    @property
    def square_millimeters(self) -> float:
        """The area in square millimeters."""
        return self._base_value / 10 ** (-3 * 2)

    @property
    def square_micrometers(self) -> float:
        """The area in square micrometers."""
        return self._base_value / 10 ** (-6 * 2)

    # --- End of auto generated part. ---


class Length(_QuantityBase):
    """The one-dimensional extent of an object or the distance between two points."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        miles: float = 0.0,
        kilometers: float = 0.0,
        meters: float = 0.0,
        feet: float = 0.0,
        inches: float = 0.0,
        centimeters: float = 0.0,
        millimeters: float = 0.0,
        micrometers: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += miles * 1609.34
        self._base_value += kilometers * 10**3
        self._base_value += meters * 1
        self._base_value += feet * 0.3048
        self._base_value += inches * 0.0254
        self._base_value += centimeters * 10**-2
        self._base_value += millimeters * 10**-3
        self._base_value += micrometers * 10**-6

    @property
    def miles(self) -> float:
        """The length in miles."""
        return self._base_value / 1609.34

    @property
    def kilometers(self) -> float:
        """The length in kilometers."""
        return self._base_value / 10**3

    @property
    def meters(self) -> float:
        """The length in meters."""
        return self._base_value / 1

    @property
    def feet(self) -> float:
        """The length in feet."""
        return self._base_value / 0.3048

    @property
    def inches(self) -> float:
        """The length in inches."""
        return self._base_value / 0.0254

    @property
    def centimeters(self) -> float:
        """The length in centimeters."""
        return self._base_value / 10**-2

    @property
    def millimeters(self) -> float:
        """The length in millimeters."""
        return self._base_value / 10**-3

    @property
    def micrometers(self) -> float:
        """The length in micrometers."""
        return self._base_value / 10**-6

    # --- End of auto generated part. ---


class Mass(_QuantityBase):
    """A measure of resistance to acceleration."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        tonnes: float = 0.0,
        kilograms: float = 0.0,
        pounds: float = 0.0,
        ounces: float = 0.0,
        grams: float = 0.0,
        milligrams: float = 0.0,
        micrograms: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += tonnes * 10**3
        self._base_value += kilograms * 1
        self._base_value += pounds * (1 / 2.20462)
        self._base_value += ounces * (1 / 35.27396)
        self._base_value += grams * 10**-3
        self._base_value += milligrams * 10**-6
        self._base_value += micrograms * 10**-9

    @property
    def tonnes(self) -> float:
        """The mass in tonnes."""
        return self._base_value / 10**3

    @property
    def kilograms(self) -> float:
        """The mass in kilograms."""
        return self._base_value / 1

    @property
    def pounds(self) -> float:
        """The mass in pounds."""
        return self._base_value / (1 / 2.20462)

    @property
    def ounces(self) -> float:
        """The mass in ounces."""
        return self._base_value / (1 / 35.27396)

    @property
    def grams(self) -> float:
        """The mass in grams."""
        return self._base_value / 10**-3

    @property
    def milligrams(self) -> float:
        """The mass in milligrams."""
        return self._base_value / 10**-6

    @property
    def micrograms(self) -> float:
        """The mass in micrograms."""
        return self._base_value / 10**-9

    # --- End of auto generated part. ---


class Velocity(_QuantityBase):
    """Distance per time."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        meters_per_second: float = 0.0,
        kilometers_per_hour: float = 0.0,
        miles_per_hour: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += meters_per_second * 1
        self._base_value += kilometers_per_hour * (1 / 3.6)
        self._base_value += miles_per_hour * (1 / 2.23694)

    @property
    def meters_per_second(self) -> float:
        """The velocity in meters per second."""
        return self._base_value / 1

    @property
    def kilometers_per_hour(self) -> float:
        """The velocity in kilometers per hour."""
        return self._base_value / (1 / 3.6)

    @property
    def miles_per_hour(self) -> float:
        """The velocity in miles per hour."""
        return self._base_value / (1 / 2.23694)

    # --- End of auto generated part. ---


class Time(_QuantityBase):
    """The duration of an event."""

    # --- This part is auto generated. Do not change manually. ---

    def __init__(
        self,
        hours: float = 0.0,
        minutes: float = 0.0,
        seconds: float = 0.0,
        milliseconds: float = 0.0,
    ) -> None:
        self._base_value = 0.0
        self._base_value += hours * 60 * 60
        self._base_value += minutes * 60
        self._base_value += seconds * 1
        self._base_value += milliseconds * 10**-3

    @property
    def hours(self) -> float:
        """The time in hours."""
        return self._base_value / 60 * 60

    @property
    def minutes(self) -> float:
        """The time in minutes."""
        return self._base_value / 60

    @property
    def seconds(self) -> float:
        """The time in seconds."""
        return self._base_value / 1

    @property
    def milliseconds(self) -> float:
        """The time in milliseconds."""
        return self._base_value / 10**-3

    # --- End of auto generated part. ---
