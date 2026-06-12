LITRES_PER_GALLON = 3.785411784


def litres_to_gallons(litres: float) -> float:
    """Convert litres to US gallons."""
    return litres / LITRES_PER_GALLON


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python litres_to_gallons.py <litres>")
        sys.exit(1)

    litres = float(sys.argv[1])
    gallons = litres_to_gallons(litres)
    print(f"{litres} litre(s) = {gallons:.6f} gallon(s)")
