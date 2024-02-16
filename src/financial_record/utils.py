def is_number(s: str, negative: bool=False ) -> bool:
    try:
        number = int(s)
        if negative:
            return number < 0
        return number > 0

    except ValueError:
        return False