def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    success = False
    try:
        for i in plant_list:
            if i is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {i}")
        success = True
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None])
    print("\nCleanup always happens, even with errors!")


test_watering_system()
