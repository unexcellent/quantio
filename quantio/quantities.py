from __future__ import annotations

from ._quantity_base import _QuantityBase


class Acceleration(_QuantityBase):
    """Rate of change of velocity."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "meters_per_square_second"

    @property
    def meters_per_square_second(self) -> float:
        """The acceleration in meters per square second."""
        return self._base_value / 1

    @property
    def g_force(self) -> float:
        """The acceleration in g force."""
        return self._base_value / (1 / 9.8)

    def __init__(
        self,
        _base_value: float = 0.0,
        meters_per_square_second: float = 0.0,
        g_force: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += meters_per_square_second * 1
        self._base_value += g_force * (1 / 9.8)

    @classmethod
    def zero(cls) -> Acceleration:
        """Create a Acceleration with a value of zero."""
        return Acceleration()

    # --- End of auto generated part. ---


class Angle(_QuantityBase):
    """The figure formed by two rays."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "radians"

    @property
    def degrees(self) -> float:
        """The angle in degrees."""
        return self._base_value / (3.141592653589793 / 180)

    @property
    def radians(self) -> float:
        """The angle in radians."""
        return self._base_value / 1

    def __init__(
        self,
        _base_value: float = 0.0,
        degrees: float = 0.0,
        radians: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += degrees * (3.141592653589793 / 180)
        self._base_value += radians * 1

    @classmethod
    def zero(cls) -> Angle:
        """Create a Angle with a value of zero."""
        return Angle()

    # --- End of auto generated part. ---


class Area(_QuantityBase):
    """The two-dimensional extent of an object."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "square_meters"

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

    def __init__(
        self,
        _base_value: float = 0.0,
        square_miles: float = 0.0,
        square_kilometers: float = 0.0,
        square_meters: float = 0.0,
        square_feet: float = 0.0,
        square_inches: float = 0.0,
        square_centimeters: float = 0.0,
        square_millimeters: float = 0.0,
        square_micrometers: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += square_miles * 1609.34**2
        self._base_value += square_kilometers * 10 ** (3 * 2)
        self._base_value += square_meters * 1
        self._base_value += square_feet * 0.3048**2
        self._base_value += square_inches * 0.0254**2
        self._base_value += square_centimeters * 10 ** (-2 * 2)
        self._base_value += square_millimeters * 10 ** (-3 * 2)
        self._base_value += square_micrometers * 10 ** (-6 * 2)

    @classmethod
    def zero(cls) -> Area:
        """Create a Area with a value of zero."""
        return Area()

    # --- End of auto generated part. ---


class ElectricalResistance(_QuantityBase):
    """A measure of an objects opposition to the flow of electric current."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "ohm"

    @property
    def gigaohm(self) -> float:
        """The electricalresistance in gigaohm."""
        return self._base_value / 10**9

    @property
    def megaohm(self) -> float:
        """The electricalresistance in megaohm."""
        return self._base_value / 10**6

    @property
    def kiloohm(self) -> float:
        """The electricalresistance in kiloohm."""
        return self._base_value / 10**3

    @property
    def ohm(self) -> float:
        """The electricalresistance in ohm."""
        return self._base_value / 1

    @property
    def milliohm(self) -> float:
        """The electricalresistance in milliohm."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        gigaohm: float = 0.0,
        megaohm: float = 0.0,
        kiloohm: float = 0.0,
        ohm: float = 0.0,
        milliohm: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += gigaohm * 10**9
        self._base_value += megaohm * 10**6
        self._base_value += kiloohm * 10**3
        self._base_value += ohm * 1
        self._base_value += milliohm * 10**-3

    @classmethod
    def zero(cls) -> ElectricalResistance:
        """Create a ElectricalResistance with a value of zero."""
        return ElectricalResistance()

    # --- End of auto generated part. ---


class ElectricCurrent(_QuantityBase):
    """The flow of charged particles moving through an electrical conductor or space."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "amperes"

    @property
    def gigaamperes(self) -> float:
        """The electriccurrent in gigaamperes."""
        return self._base_value / 10**9

    @property
    def megaamperes(self) -> float:
        """The electriccurrent in megaamperes."""
        return self._base_value / 10**6

    @property
    def kiloamperes(self) -> float:
        """The electriccurrent in kiloamperes."""
        return self._base_value / 10**3

    @property
    def amperes(self) -> float:
        """The electriccurrent in amperes."""
        return self._base_value / 1

    @property
    def milliamperes(self) -> float:
        """The electriccurrent in milliamperes."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        gigaamperes: float = 0.0,
        megaamperes: float = 0.0,
        kiloamperes: float = 0.0,
        amperes: float = 0.0,
        milliamperes: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += gigaamperes * 10**9
        self._base_value += megaamperes * 10**6
        self._base_value += kiloamperes * 10**3
        self._base_value += amperes * 1
        self._base_value += milliamperes * 10**-3

    @classmethod
    def zero(cls) -> ElectricCurrent:
        """Create a ElectricCurrent with a value of zero."""
        return ElectricCurrent()

    # --- End of auto generated part. ---


class Energy(_QuantityBase):
    """Energy describes the ability of an object to perform work."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "joules"

    @property
    def gigajoules(self) -> float:
        """The energy in gigajoules."""
        return self._base_value / 10**9

    @property
    def megajoules(self) -> float:
        """The energy in megajoules."""
        return self._base_value / 10**6

    @property
    def kilojoules(self) -> float:
        """The energy in kilojoules."""
        return self._base_value / 10**3

    @property
    def joules(self) -> float:
        """The energy in joules."""
        return self._base_value / 1

    @property
    def millijoules(self) -> float:
        """The energy in millijoules."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        gigajoules: float = 0.0,
        megajoules: float = 0.0,
        kilojoules: float = 0.0,
        joules: float = 0.0,
        millijoules: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += gigajoules * 10**9
        self._base_value += megajoules * 10**6
        self._base_value += kilojoules * 10**3
        self._base_value += joules * 1
        self._base_value += millijoules * 10**-3

    @classmethod
    def zero(cls) -> Energy:
        """Create a Energy with a value of zero."""
        return Energy()

    # --- End of auto generated part. ---


class Frequency(_QuantityBase):
    """The number of occurrences of a repeating event per unit of time."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "hertz"

    @property
    def gigahertz(self) -> float:
        """The frequency in gigahertz."""
        return self._base_value / 10**9

    @property
    def megahertz(self) -> float:
        """The frequency in megahertz."""
        return self._base_value / 10**6

    @property
    def kilohertz(self) -> float:
        """The frequency in kilohertz."""
        return self._base_value / 10**3

    @property
    def hertz(self) -> float:
        """The frequency in hertz."""
        return self._base_value / 1

    def __init__(
        self,
        _base_value: float = 0.0,
        gigahertz: float = 0.0,
        megahertz: float = 0.0,
        kilohertz: float = 0.0,
        hertz: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += gigahertz * 10**9
        self._base_value += megahertz * 10**6
        self._base_value += kilohertz * 10**3
        self._base_value += hertz * 1

    @classmethod
    def zero(cls) -> Frequency:
        """Create a Frequency with a value of zero."""
        return Frequency()

    # --- End of auto generated part. ---


class Length(_QuantityBase):
    """The one-dimensional extent of an object or the distance between two points."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "meters"

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

    def __init__(
        self,
        _base_value: float = 0.0,
        miles: float = 0.0,
        kilometers: float = 0.0,
        meters: float = 0.0,
        feet: float = 0.0,
        inches: float = 0.0,
        centimeters: float = 0.0,
        millimeters: float = 0.0,
        micrometers: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += miles * 1609.34
        self._base_value += kilometers * 10**3
        self._base_value += meters * 1
        self._base_value += feet * 0.3048
        self._base_value += inches * 0.0254
        self._base_value += centimeters * 10**-2
        self._base_value += millimeters * 10**-3
        self._base_value += micrometers * 10**-6

    @classmethod
    def zero(cls) -> Length:
        """Create a Length with a value of zero."""
        return Length()

    # --- End of auto generated part. ---


class Mass(_QuantityBase):
    """A measure of resistance to acceleration."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "kilograms"

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

    def __init__(
        self,
        _base_value: float = 0.0,
        tonnes: float = 0.0,
        kilograms: float = 0.0,
        pounds: float = 0.0,
        ounces: float = 0.0,
        grams: float = 0.0,
        milligrams: float = 0.0,
        micrograms: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += tonnes * 10**3
        self._base_value += kilograms * 1
        self._base_value += pounds * (1 / 2.20462)
        self._base_value += ounces * (1 / 35.27396)
        self._base_value += grams * 10**-3
        self._base_value += milligrams * 10**-6
        self._base_value += micrograms * 10**-9

    @classmethod
    def zero(cls) -> Mass:
        """Create a Mass with a value of zero."""
        return Mass()

    # --- End of auto generated part. ---


class Power(_QuantityBase):
    """The amount of energy transferred or converted per unit time."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "watts"

    @property
    def gigawatts(self) -> float:
        """The power in gigawatts."""
        return self._base_value / 10**9

    @property
    def megawatts(self) -> float:
        """The power in megawatts."""
        return self._base_value / 10**6

    @property
    def kilowatts(self) -> float:
        """The power in kilowatts."""
        return self._base_value / 10**3

    @property
    def watts(self) -> float:
        """The power in watts."""
        return self._base_value / 1

    @property
    def milliwatts(self) -> float:
        """The power in milliwatts."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        gigawatts: float = 0.0,
        megawatts: float = 0.0,
        kilowatts: float = 0.0,
        watts: float = 0.0,
        milliwatts: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += gigawatts * 10**9
        self._base_value += megawatts * 10**6
        self._base_value += kilowatts * 10**3
        self._base_value += watts * 1
        self._base_value += milliwatts * 10**-3

    @classmethod
    def zero(cls) -> Power:
        """Create a Power with a value of zero."""
        return Power()

    # --- End of auto generated part. ---


class Time(_QuantityBase):
    """The duration of an event."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "seconds"

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

    def __init__(
        self,
        _base_value: float = 0.0,
        hours: float = 0.0,
        minutes: float = 0.0,
        seconds: float = 0.0,
        milliseconds: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += hours * 60 * 60
        self._base_value += minutes * 60
        self._base_value += seconds * 1
        self._base_value += milliseconds * 10**-3

    @classmethod
    def zero(cls) -> Time:
        """Create a Time with a value of zero."""
        return Time()

    # --- End of auto generated part. ---


class Velocity(_QuantityBase):
    """Distance per time."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "meters_per_second"

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

    def __init__(
        self,
        _base_value: float = 0.0,
        meters_per_second: float = 0.0,
        kilometers_per_hour: float = 0.0,
        miles_per_hour: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += meters_per_second * 1
        self._base_value += kilometers_per_hour * (1 / 3.6)
        self._base_value += miles_per_hour * (1 / 2.23694)

    @classmethod
    def zero(cls) -> Velocity:
        """Create a Velocity with a value of zero."""
        return Velocity()

    # --- End of auto generated part. ---


class Voltage(_QuantityBase):
    """The difference in electric potential between two points."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "volts"

    @property
    def gigavolts(self) -> float:
        """The voltage in gigavolts."""
        return self._base_value / 10**9

    @property
    def megavolts(self) -> float:
        """The voltage in megavolts."""
        return self._base_value / 10**6

    @property
    def kilovolts(self) -> float:
        """The voltage in kilovolts."""
        return self._base_value / 10**3

    @property
    def volts(self) -> float:
        """The voltage in volts."""
        return self._base_value / 1

    @property
    def millivolts(self) -> float:
        """The voltage in millivolts."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        gigavolts: float = 0.0,
        megavolts: float = 0.0,
        kilovolts: float = 0.0,
        volts: float = 0.0,
        millivolts: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += gigavolts * 10**9
        self._base_value += megavolts * 10**6
        self._base_value += kilovolts * 10**3
        self._base_value += volts * 1
        self._base_value += millivolts * 10**-3

    @classmethod
    def zero(cls) -> Voltage:
        """Create a Voltage with a value of zero."""
        return Voltage()

    # --- End of auto generated part. ---
