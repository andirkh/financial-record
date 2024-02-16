import sys

# Local modules :
from render import render
from utils import is_number, yes_or_no_input
from actions import record_transaction, \
    get_transaction_in, \
    get_transaction_out, \
    get_sum_in, \
    get_sum_out, \
    get_sum_all, \
    reset_transactions

def main():
    render()
    while True:
        user_input: str = input("Prompt > ").strip()

        if user_input == 'a':
            transaction_in = get_transaction_in()
            render(record=f"list uang masuk: {repr(transaction_in)}")
        elif user_input == 'b':
            transaction_out = get_transaction_out()
            render(record=f"list uang keluar: {repr(transaction_out)}")
        elif user_input == 'c':
            sum_in = get_sum_in()
            render(record=f"jumlah uang masuk: {str(sum_in)}")
        elif user_input == 'd':
            sum_out = get_sum_out()
            render(record=f"jumlah uang keluar: {str(sum_out)}")
        elif user_input == 'e':
            sum_all = get_sum_all()
            render(record=f"saldo: {str(sum_all)}")
        elif user_input == 'exit':
            sys.exit()
        elif user_input == 'reset':
            continue_reset = yes_or_no_input()
            if continue_reset:
                reset_transactions()
                render(record="Semua transaksi terhapus 🙏")
            else:
                render(record="reset dibatalkan 👌")

        # Record any transaction
        elif is_number(user_input, negative=False):
            record_transaction(user_input)
            render(record=f"{user_input} berhasil ditambahkan")
        elif is_number(user_input, negative=True):
            record_transaction(user_input)
            render(record=f"{user_input} berhasil dikeluarkan")
        else:
            render(record="command not found")

if __name__ == "__main__":
    main()