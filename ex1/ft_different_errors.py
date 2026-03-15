def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")

    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        my_dict = {"tomato": 1}
        my_dict["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("Testing multiple errors together...")
    try:
        1 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


test_error_types()
