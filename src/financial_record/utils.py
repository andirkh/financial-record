def is_number(s: str, negative: bool=False ) -> bool:
    try:
        number = int(s)
        if negative:
            return number < 0
        return number > 0

    except ValueError:
        return False

def yes_or_no_input() -> bool:
    response = input("Are you sure? (y/N)").lower()
    return response == "y"
