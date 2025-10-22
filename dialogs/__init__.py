from aiogram_dialog import Dialog
from dialogs.start import start_window, first_time_window
from dialogs.settings import settings_window, difficulty_choice, theme_choice
from dialogs.profile import profile_window
from dialogs.invoice import invoice_window
from dialogs.game import game_window

start_dialog = Dialog(
    first_time_window,
    start_window
)

settings_dialog = Dialog(
    settings_window,
    difficulty_choice,
    theme_choice
)

profile_dialog = Dialog(
    profile_window
)

invoice_dialog = Dialog(
    invoice_window
)

game_dialog = Dialog(
    game_window
)