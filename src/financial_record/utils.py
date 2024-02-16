import locale
from typing import List

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

def format_idr(amount: int) -> str:
    return "Rp. {:,.0f}".format(amount).replace(",", ".")

def format_array_idr(amounts: List[int]) -> str:
    return [format_idr(x) for x in amounts]