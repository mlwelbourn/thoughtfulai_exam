


def sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


