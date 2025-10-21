from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Cancel

from states.states import InvoiceSG

# todo: Доделать invoice
invoice_window = Window(
    Const("Поддержка разработчика"),
    Button(Const("Платежка(in_dev)"), id="invoice"),
    Cancel(Const("⬅️ Назад")),
    state=InvoiceSG.main
)
