from rich.layout import Layout
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import Console

from actions import push_history, get_history

def Header_Panel() -> Panel:
    return Panel("[Group-10] Financial Record", style="bold white on blue", height=3)

def Record_Panel(output: str) -> Panel:
    history = get_history()
    history_message =  ""

    if len(history) > 0:
        printed_history = '\n'.join(f'- {x}' for x in history)
        history_message=f"""
---
## 🕦 History:
{printed_history}
"""
    
    message: str = f"""
## 💵 Record:
# ⭐️ {output} ⭐️

{history_message}
"""
    return Panel(Markdown(message), style="white on black")


def Guide_Panel() -> Panel:
    message: str = """
## 📄 Menu:
- *a* (list uang masuk)
- *b* (list uang keluar)
- *c* (jumlah uang masuk)    
- *d* (jumlah uang keluar)
- *e* (saldo)
---
## 🖥  Input:
- *1000* (in)
- *-1000* (out)
---
## 🚪 Others:
- *undo*
- *exit* (keluar)
- *reset* (hapus semua)
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
    push_history(record)

    layout = make_layout()
    layout['header'].update(Header_Panel())
    layout['main-right'].update(Guide_Panel())
    layout['main-left'].update(Record_Panel(output=record))
    Console().print(layout)