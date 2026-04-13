def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    data_valide: str = "25"
    print(f"Input data is '{data_valide}'")
    try:
        res_valide: int = input_temperature(data_valide)
        print(f"Temperature is now {res_valide}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    data_invalide: str = "abc"
    print(f"Input data is '{data_invalide}'")
    try:
        res_invalide: int = input_temperature(data_invalide)
        print(f"Temperature is now {res_invalide}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed- program didn't crash!")


if __name__ == "__main__":
    test_temperature()
