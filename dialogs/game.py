from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel, Select, Group, Row, Button

import json

from states.states import GameSG
from services.victorina import Victorina
from database.database import Database

json_string = '''[{"id": 5752,"question": "How do you use 'mapState' to access the state of a specific Vuex module?","description": "Learning how to map module state to component properties using 'mapState'.","answers": {"answer_a": "mapState(['stateProperty'])","answer_b": "mapState('moduleName', ['stateProperty'])","answer_c": "mapState('stateProperty')","answer_d": "mapState('moduleName/stateProperty')","answer_e": null,"answer_f": null},"multiple_correct_answers": "false","correct_answers": {"answer_a_correct": "false","answer_b_correct": "true","answer_c_correct": "false","answer_d_correct": "false","answer_e_correct": "false","answer_f_correct": "false"},"correct_answer": null,"explanation": "You use 'mapState('moduleName', ['stateProperty'])' to access and map a specific module's state properties to component properties.","tip": null,"tags": [{"name": "VueJS"}],"category": "VueJS","difficulty": "Medium"}]'''
data = json.loads(json_string)

async def get_question_info(dialog_manager: DialogManager, **kwargs):
    return await update_next_question(dialog_manager)

async def update_next_question(manager: DialogManager):
    user_id = manager.event.from_user.id
    db: Database = manager.middleware_data.get("db")

    category_data = await db.get_category(user_id)
    difficulty_data = await db.get_difficulty(user_id)

    category = category_data['theme'] if category_data else None
    difficulty = difficulty_data['difficulty'] if difficulty_data else None

    victorina = Victorina(
        category=category if category.lower() != 'all' else None,
        difficulty=difficulty
    )

    answers = victorina.get_answers()
    correct_answer_key = victorina.get_correct_answer_key().replace('_correct', '')
    correct_answer_text = answers.get(correct_answer_key, "Неизвестный ответ")
    manager.dialog_data['correct_answer_text'] = correct_answer_text
    manager.dialog_data['correct_answer'] = correct_answer_key

    return {
        'question': victorina.get_question(),
        'answers': list(victorina.get_answers().items())
    }

async def get_right_answer_text(dialog_manager: DialogManager, **kwargs):
    correct_answer_text = dialog_manager.dialog_data.get("correct_answer_text", "Неизвестный ответ")
    return {
        'right_answer': correct_answer_text
    }

async def on_answer_selected(callback, button, manager: DialogManager, item_id: str):
    user_answer = item_id
    correct_answer = manager.dialog_data.get("correct_answer")
    user_id = manager.event.from_user.id
    db : Database = manager.middleware_data.get("db")

    if (user_answer == correct_answer):
        await db.increment_wins(user_id)
        await manager.switch_to(GameSG.correct_result)
    else:
        await db.increment_games(user_id)
        await manager.switch_to(GameSG.incorrect_result)
    

async def to_next_question(callback, button, manager: DialogManager):
    manager.dialog_data.pop('correct_answer', None)
    manager.dialog_data.pop('correct_answer_text', None)
    await manager.switch_to(GameSG.question)

game_window = Window(
    Format("❓ Вопрос:\n{question}"),
    
    Group(
        Select(
            text=Format("{item[1]}"),
            id="answers_select",
            item_id_getter=lambda item: item[0],
            items="answers",
            on_click=on_answer_selected,
        ),
        width=1,
    ),
    
    Cancel(Const("⬅️ Выйти")),
    
    getter=get_question_info,
    state=GameSG.question
)

win_window = Window(
    Const("✅ Правильный ответ!"),
    Row(
        Cancel(Const("В меню")),
        Button(Const("Следующий вопрос"), id="to_next_question", on_click=to_next_question)
    ),
    state=GameSG.correct_result
)

lose_window = Window(
    Const("❌ Неправильный ответ!"),
    Format("Правильный ответ: {right_answer}"),
    Row(
        Cancel(Const("В меню")),
        Button(Const("Следующий вопрос"), id="to_next_question", on_click=to_next_question)
    ),
    getter=get_right_answer_text,
    state=GameSG.incorrect_result
)