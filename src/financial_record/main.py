import sys

# Local modules :
from render import render
from utils import is_number, \
    yes_or_no_input, \
    format_idr, \
    format_array_idr
from actions import record_transaction, \
    get_transaction_in, \
    get_transaction_out, \
    get_sum_in, \
    get_sum_out, \
    get_sum_all, \
    get_last_transaction, \
    reset_transactions, \
    undo_transactions

def main():
    render()
    while True:
        prompt: str = input("Prompt > ").strip()

        if prompt == 'a':
            transaction_in = get_transaction_in()
            render(record=f"list uang masuk: {repr(format_array_idr(transaction_in))}")
        elif prompt == 'b':
            transaction_out = get_transaction_out()
            render(record=f"list uang keluar: {repr(format_array_idr(transaction_out))}")
        elif prompt == 'c':
            sum_in = get_sum_in()
            render(record=f"jumlah uang masuk: {format_idr(sum_in)}")
        elif prompt == 'd':
            sum_out = get_sum_out()
            render(record=f"jumlah uang keluar: {format_idr(sum_out)}")
        elif prompt == 'e':
            sum_all = get_sum_all()
            render(record=f"saldo: {format_idr(sum_all)}")
        elif prompt == 'undo':
            transactions = get_transaction_in()
            if len(transactions) > 0:
                last_transaction = get_last_transaction()
                undo_transactions()
                render(record=f"⎌ (undo) {format_idr(last_transaction)} tidak jadi dimasukkan")
            else:
                render(record="Gagal undo, tdk ada transaksi yg tersisa 🙏")
        elif prompt == 'exit':
            sys.exit()
        elif prompt == 'reset':
            continue_reset = yes_or_no_input()
            if continue_reset:
                reset_transactions()
                render(record="(reset) Semua transaksi terhapus 🙏")
            else:
                render(record="reset dibatalkan 👌")

        # Record any transaction
        elif is_number(prompt, negative=False):
            input_number = int(prompt)
            record_transaction(input_number)
            render(record=f"📀 {format_idr(input_number)} masuk")

        elif is_number(prompt, negative=True):
            input_number = int(prompt)
            record_transaction(input_number)
            render(record=f"📀 {format_idr(abs(input_number))} keluar")
        else:
            render(record="command not found")

if __name__ == "__main__":
    main()