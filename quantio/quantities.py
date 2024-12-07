from __future__ import annotations

from abc import ABC

from .exceptions import CanNotAddTypesError, CanNotSubtractTypesError


class Quantity(ABC):
    """Parent class to all quantities."""

    _base_value: float
    "The base unit of the quantity."

    BASE_UNIT: str
    "Name of the unit with a factor of 1."

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if isinstance(other, type(self)):
            return self._base_value == other._base_value

        return False

    def __add__(self, other: Quantity) -> Quantity:
        """Add two quantities of the same type."""
        if type(self) is not type(other):
            raise CanNotAddTypesError(self.__class__.__name__, other.__class__.__name__)

        result = type(self)()
        result._base_value = self._base_value + other._base_value
        return result

    def __sub__(self, other: Quantity) -> Quantity:
        """Subtract two quantities of the same type."""
        if type(self) is not type(other):
            raise CanNotSubtractTypesError(self.__class__.__name__, other.__class__.__name__)

        result = type(self)()
        result._base_value = self._base_value - other._base_value
        return result

    def __repr__(self) -> str:
        """Return an unambiguous representation of this quantity."""
        return self.__str__()


class Acceleration(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Acceleration(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Angle(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Angle(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class AngularVelocity(Quantity):
    """The change in angle per time."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "radians_per_second"

    @property
    def degrees_per_second(self) -> float:
        """The angularvelocity in degrees per second."""
        return self._base_value / (3.141592653589793 / 180)

    @property
    def radians_per_second(self) -> float:
        """The angularvelocity in radians per second."""
        return self._base_value / 1

    def __init__(
        self,
        _base_value: float = 0.0,
        degrees_per_second: float = 0.0,
        radians_per_second: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += degrees_per_second * (3.141592653589793 / 180)
        self._base_value += radians_per_second * 1

    @classmethod
    def zero(cls) -> AngularVelocity:
        """Create a AngularVelocity with a value of zero."""
        return AngularVelocity()

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "AngularVelocity(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Area(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Area(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Density(Quantity):
    """A substance's mass per unit of volume."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "kilograms_per_cubic_meter"

    @property
    def grams_per_cubic_meter(self) -> float:
        """The density in grams per cubic meter."""
        return self._base_value / 10**3

    @property
    def kilograms_per_cubic_meter(self) -> float:
        """The density in kilograms per cubic meter."""
        return self._base_value / 1

    @property
    def kilograms_per_liter(self) -> float:
        """The density in kilograms per liter."""
        return self._base_value / 10**-3

    @property
    def grams_per_milliliter(self) -> float:
        """The density in grams per milliliter."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        grams_per_cubic_meter: float = 0.0,
        kilograms_per_cubic_meter: float = 0.0,
        kilograms_per_liter: float = 0.0,
        grams_per_milliliter: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += grams_per_cubic_meter * 10**3
        self._base_value += kilograms_per_cubic_meter * 1
        self._base_value += kilograms_per_liter * 10**-3
        self._base_value += grams_per_milliliter * 10**-3

    @classmethod
    def zero(cls) -> Density:
        """Create a Density with a value of zero."""
        return Density()

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Density(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class ElectricalResistance(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "ElectricalResistance(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class ElectricCurrent(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "ElectricCurrent(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Energy(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Energy(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Frequency(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Frequency(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Length(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Length(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Mass(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Mass(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Power(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Power(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Pressure(Quantity):
    """The amount of force per unit area."""

    # --- This part is auto generated. Do not change manually. ---

    BASE_UNIT = "kilopascal"

    @property
    def terapascal(self) -> float:
        """The pressure in terapascal."""
        return self._base_value / 10**9

    @property
    def gigapascal(self) -> float:
        """The pressure in gigapascal."""
        return self._base_value / 10**6

    @property
    def megapascal(self) -> float:
        """The pressure in megapascal."""
        return self._base_value / 10**3

    @property
    def kilopascal(self) -> float:
        """The pressure in kilopascal."""
        return self._base_value / 1

    @property
    def bar(self) -> float:
        """The pressure in bar."""
        return self._base_value / 10**-2

    @property
    def pascal(self) -> float:
        """The pressure in pascal."""
        return self._base_value / 10**-3

    @property
    def millipascal(self) -> float:
        """The pressure in millipascal."""
        return self._base_value / 10**-3

    def __init__(
        self,
        _base_value: float = 0.0,
        terapascal: float = 0.0,
        gigapascal: float = 0.0,
        megapascal: float = 0.0,
        kilopascal: float = 0.0,
        bar: float = 0.0,
        pascal: float = 0.0,
        millipascal: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += terapascal * 10**9
        self._base_value += gigapascal * 10**6
        self._base_value += megapascal * 10**3
        self._base_value += kilopascal * 1
        self._base_value += bar * 10**-2
        self._base_value += pascal * 10**-3
        self._base_value += millipascal * 10**-3

    @classmethod
    def zero(cls) -> Pressure:
        """Create a Pressure with a value of zero."""
        return Pressure()

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Pressure(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Time(Quantity):
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

    @property
    def microseconds(self) -> float:
        """The time in microseconds."""
        return self._base_value / 10**-6

    @property
    def nanoseconds(self) -> float:
        """The time in nanoseconds."""
        return self._base_value / 10**-9

    def __init__(
        self,
        _base_value: float = 0.0,
        hours: float = 0.0,
        minutes: float = 0.0,
        seconds: float = 0.0,
        milliseconds: float = 0.0,
        microseconds: float = 0.0,
        nanoseconds: float = 0.0,
    ) -> None:
        self._base_value = _base_value
        self._base_value += hours * 60 * 60
        self._base_value += minutes * 60
        self._base_value += seconds * 1
        self._base_value += milliseconds * 10**-3
        self._base_value += microseconds * 10**-6
        self._base_value += nanoseconds * 10**-9

    @classmethod
    def zero(cls) -> Time:
        """Create a Time with a value of zero."""
        return Time()

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Time(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Velocity(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Velocity(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---


class Voltage(Quantity):
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

    def __str__(self) -> str:
        """Display this quantity as a string for printing."""
        return "Voltage(" + self.BASE_UNIT + "=" + str(self._base_value) + ")"

    # --- End of auto generated part. ---
