LITRES_PER_GALLON = 3.785411784


def litres_to_gallons(litres):
    """Convert litres to US gallons."""
    return litres / LITRES_PER_GALLON


if __name__ == "__main__":
    examples = [1, 5, 10, 50, 100]
    for value in examples:
        print(f"{value} litre(s) = {litres_to_gallons(value):.4f} gallon(s)")
