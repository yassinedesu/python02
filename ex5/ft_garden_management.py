class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, name: str) -> None:
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(name)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        success = False
        try:
            for plant in self.plants:
                if plant is None:
                    raise ValueError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
            success = True
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!")

    def check_plant_health(
            self, name: str, water: int, sun: int
            ) -> str | None:

        try:
            if not name:
                raise ValueError("Plant name cannot be empty!")

            if water < 1 or water > 10:
                if water > 10:
                    raise ValueError(
                        f"Water level {water} is too high (max 10)"
                        )
                if water < 1:
                    raise ValueError(f"Water level {water} is too low (min 1)")

            if sun < 2 or sun > 12:
                if sun < 2:
                    raise ValueError(
                        f"Sunlight hours {sun} is too low (min 2)"
                        )
                if sun > 12:
                    raise ValueError(
                        f"Sunlight hours {sun} is too high (max 12)"
                        )
            print(f"{name}: healthy (water: {water}, sun: {sun})")
        except ValueError as e:
            print(f"Error checking {name}: {e}")


def test_garden_management() -> None:
    garden = GardenManager()
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    garden.add_plant("")

    print("Watering plants...")
    garden.water_plants()

    print("Checking plant health...")
    garden.check_plant_health("tomato", 5, 8)
    garden.check_plant_health("lettuce", 15, 8)
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


test_garden_management()
