from src.financial_record.actions \
      import record_transaction, \
             records

def test_records() -> None:
  record_transaction(1000)
  assert records[0] == 1000

if __name__ == "__main__":
    test_records()
                                        

