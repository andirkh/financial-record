from rich import print as renderUI
from rich.layout import Layout
from rich.panel import Panel
from rich.markdown import Markdown

def Header_Panel() -> Panel:
    return Panel("Task-3: Group 10 (Financial Record)", style="bold white on blue", height=3)

def Record_Panel(record: str) -> Panel:
    message: str = f"""## Record:
    {record}
    """
    return Panel(Markdown(message), style="white on black")

def Guide_Panel() -> Panel:
    message: str = """## Menu:
    > a (list uang masuk)
    > b (list uang keluar)
    > c (jumlah uang masuk)    
    > d (jumlah uang keluar)
    > e (saldo)
    
    > 1000 (memasukkan 1000)
    > -1000 (mengeluarkan 1000)

    > undo
    > exit (keluar)
    > reset (hapus semua)
    """
    return Panel(Markdown(message), style="green on black")


def make_layout() -> Layout:
    layout = Layout(name="root")

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
    )

    layout["main"].split_row(
        Layout(name="main-left", ratio=7),
        Layout(name="main-right", ratio=3),
    )

    return layout

def render(record: str="") -> None:
    layout = make_layout()
    layout['header'].update(Header_Panel())
    layout['main-left'].update(Record_Panel(record))
    layout['main-right'].update(Guide_Panel())
    renderUI(layout)