from typing import List

# State
records: List[int] = [];

def record_transaction(input_number: str) -> None:
  records.append(int(input_number))

def get_transaction_in() -> List[int]:
  return [x for x in records if x > 0]

def get_transaction_out() -> List[int]:
  return [x for x in records if x < 0]

def get_sum_in() -> int:
  return sum(get_transaction_in())

def get_sum_out() -> int:
  return sum(get_transaction_out())

def get_sum_all() -> int:
  return sum(records)

def reset_transactions() -> None:
  records.clear()