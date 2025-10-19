from aiogram.fsm.state import State, StatesGroup

class MainMenu(StatesGroup):
    main = State()
    game = State()
    settings = State()
    profile = State()
    support = State()

