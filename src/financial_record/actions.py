from typing import List

# State
records: List[int] = [];
history: List[str] = [];

def record_transaction(input_number: int) -> None:
  records.append(input_number)

def reset_transactions() -> None:
  records.clear()

def undo_transactions() -> None:
  if len(records) > 0:
    records.pop()

def push_history(record: str) -> None:
  if len(record) > 0:
    history.append(record)

def get_last_transaction() -> int:
  if len(records) > 0:
    return records[-1]

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

def get_history() -> List[str]:
  if len(history) > 0:
    reversed_history = history[::-1]
    return reversed_history[1:15]
  return []