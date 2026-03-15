def check_temperature(temp_str: str) -> int | None:
    try:
        data = int(temp_str)
        if data >= 0 and data <= 40:
            print(f"Temperature {data}°C is perfect for plants!\n")
            return data
        elif data > 40:
            print(f"Error: {data}°C is too hot for plants (max 40°C)\n")
        elif data < 0:
            print(f"Error: {data}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


test_temperature_input()
