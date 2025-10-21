from aiogram.fsm.state import State, StatesGroup

class MainSG(StatesGroup):
    main = State()     # Стартовое меню

class GameSG(StatesGroup):
    question = State()
    result = State()

class SettingsSG(StatesGroup):
    main = State()
    difficulty = State()
    category = State()

class ProfileSG(StatesGroup):
    main = State()

class InvoiceSG(StatesGroup):
    main = State()
