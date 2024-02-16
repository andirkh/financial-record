import sys

# Local modules :
from render import render
from utils import is_number

def main():
    render()
    while True:
        user_input: str = input("Prompt > ").strip()

        if user_input == 'a':
            render(record="list uang masuk")
        elif user_input == 'b':
            render(record="list uang keluar")
        elif user_input == 'c':
            render(record="jumlah uang masuk")
        elif user_input == 'd':
            render(record="jumlah uang keluar")
        elif user_input == 'e':
            render(record="saldo")
        elif user_input == 'exit':
            sys.exit()
        elif is_number(user_input, negative=False):
            render(record=f"{user_input} berhasil ditambahkan")
        elif is_number(user_input, negative=True):
            render(record=f"{user_input} berhasil dikeluarkan")
        else:
            render(record="command not found")

if __name__ == "__main__":
    main()