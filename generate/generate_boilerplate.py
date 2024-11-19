from __future__ import annotations

from pathlib import Path

TARGET_FILE_PATH = Path(__file__).parent.parent / "quantio" / "quantities.py"


def generate_boilerplate(quantities_with_fields: dict[str, dict[str, str]]) -> None:
    """Generate the boilerplate parts of the quantity classes."""
    with TARGET_FILE_PATH.open() as target_file:
        target_content = target_file.readlines()

    target_content_with_boilerplate = []
    current_class: str | None = None

    current_line_is_part_of_autogenerated_code = False
    for line in target_content:
        if line.startswith("class "):
            current_class = line.split("(")[0][6:]

        if "# --- This part is auto generated. Do not change manually. ---" in line:
            current_line_is_part_of_autogenerated_code = True
            target_content_with_boilerplate.append(line)
            target_content_with_boilerplate.append("")
            target_content_with_boilerplate.extend(
                _generate_base_unit(current_class, quantities_with_fields[current_class])
            )
            target_content_with_boilerplate.extend(
                _generate_properties(current_class, quantities_with_fields[current_class])
            )
            target_content_with_boilerplate.extend(
                _generate_init(quantities_with_fields[current_class])
            )
            target_content_with_boilerplate.extend(_generat_zero_function(current_class))

        if "# --- End of auto generated part. ---" in line:
            current_line_is_part_of_autogenerated_code = False

        if current_line_is_part_of_autogenerated_code:
            continue

        target_content_with_boilerplate.append(line)

    for line_number, line in enumerate(target_content_with_boilerplate):
        if not line.endswith("\n"):
            target_content_with_boilerplate[line_number] += "\n"

    with TARGET_FILE_PATH.open("w") as target_file:
        target_file.writelines(target_content_with_boilerplate)


def _generate_base_unit(current_class: str, units: dict[str, str]) -> list[str]:
    base_unit = None
    for unit, factor in units.items():
        if float(eval(factor)) == 1:
            base_unit = unit
            break

    if base_unit is None:
        raise ValueError(f"{current_class} needs a unit with factor equal to 1.")

    return [f'    BASE_UNIT = "{base_unit}"', ""]


def _generate_properties(current_class: str, units: dict[str, str]) -> list[str]:
    code = []

    for unit, factor in units.items():
        code.append(" " * 4 + "@property")
        code.append(" " * 4 + f"def {unit}(self) -> float:")
        code.append(" " * 8 + f'"""The {current_class.lower()} in {unit.replace("_", " ")}."""')
        code.append(" " * 8 + f"return self._base_value / {factor}")
        code.append("")

    return code


def _generate_init(units: dict[str, str]) -> list[str]:
    code = [" " * 4 + "def __init__(", " " * 8 + "self,", " " * 8 + "_base_value: float = 0.0,"]

    for unit in units:
        code.append(" " * 8 + f"{unit}: float = 0.0,")

    code.append(" " * 4 + ") -> None:")
    code.append(" " * 8 + "self._base_value = _base_value")

    for unit, factor in units.items():
        code.append(" " * 8 + f"self._base_value += {unit} * {factor}")

    code.append("")
    return code


def _generat_zero_function(current_class: str) -> list[str]:
    return [
        " " * 4 + "@classmethod",
        " " * 4 + f"def zero(cls) -> {current_class}:",
        " " * 8 + f'"""Create a {current_class} with a value of zero."""',
        " " * 8 + f"return {current_class}()",
        "",
    ]


if __name__ == "__main__":
    quantities_with_fields = {
        "Acceleration": {
            "meters_per_square_second": "1",
            "g_force": "(1 / 9.8)",
        },
        "Angle": {
            "degrees": "(3.141592653589793 / 180)",
            "radians": "1",
        },
        "Area": {
            "square_miles": "1609.34**2",
            "square_kilometers": "10 ** (3 * 2)",
            "square_meters": "1",
            "square_feet": "0.3048**2",
            "square_inches": "0.0254**2",
            "square_centimeters": "10 ** (-2 * 2)",
            "square_millimeters": "10 ** (-3 * 2)",
            "square_micrometers": "10 ** (-6 * 2)",
        },
        "ElectricalResistance": {
            "gigaohm": "10**9",
            "megaohm": "10**6",
            "kiloohm": "10**3",
            "ohm": "1",
            "milliohm": "10**-3",
        },
        "Energy": {
            "gigajoules": "10**9",
            "megajoules": "10**6",
            "kilojoules": "10**3",
            "joules": "1",
            "millijoules": "10**-3",
        },
        "Frequency": {
            "gigahertz": "10**9",
            "megahertz": "10**6",
            "kilohertz": "10**3",
            "hertz": "1",
        },
        "Length": {
            "miles": "1609.34",
            "kilometers": "10**3",
            "meters": "1",
            "feet": "0.3048",
            "inches": "0.0254",
            "centimeters": "10**-2",
            "millimeters": "10**-3",
            "micrometers": "10**-6",
        },
        "Mass": {
            "tonnes": "10**3",
            "kilograms": "1",
            "pounds": "(1 / 2.20462)",
            "ounces": "(1 / 35.27396)",
            "grams": "10**-3",
            "milligrams": "10**-6",
            "micrograms": "10**-9",
        },
        "Power": {
            "gigawatts": "10**9",
            "megawatts": "10**6",
            "kilowatts": "10**3",
            "watts": "1",
            "milliwatts": "10**-3",
        },
        "Velocity": {
            "meters_per_second": "1",
            "kilometers_per_hour": "(1 / 3.6)",
            "miles_per_hour": "(1 / 2.23694)",
        },
        "Time": {
            "hours": "60 * 60",
            "minutes": "60",
            "seconds": "1",
            "milliseconds": "10**-3",
        },
    }

    generate_boilerplate(quantities_with_fields)
