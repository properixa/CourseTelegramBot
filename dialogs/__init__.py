from aiogram_dialog import Dialog
from dialogs.start import start_window
from dialogs.settings import settings_window, difficulty_choice, theme_choice

start_dialog = Dialog(start_window)
settings_dialog = Dialog(
    settings_window,
    difficulty_choice,
    theme_choice
)