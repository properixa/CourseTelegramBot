from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Row, Cancel, Select
from aiogram_dialog import ShowMode
import json

from states.states import GameSG
from services.victorina import Victorina

json_string = '''[{"id": 5752,"question": "How do you use 'mapState' to access the state of a specific Vuex module?","description": "Learning how to map module state to component properties using 'mapState'.","answers": {"answer_a": "mapState(['stateProperty'])","answer_b": "mapState('moduleName', ['stateProperty'])","answer_c": "mapState('stateProperty')","answer_d": "mapState('moduleName/stateProperty')","answer_e": null,"answer_f": null},"multiple_correct_answers": "false","correct_answers": {"answer_a_correct": "false","answer_b_correct": "true","answer_c_correct": "false","answer_d_correct": "false","answer_e_correct": "false","answer_f_correct": "false"},"correct_answer": null,"explanation": "You use 'mapState('moduleName', ['stateProperty'])' to access and map a specific module's state properties to component properties.","tip": null,"tags": [{"name": "VueJS"}],"category": "VueJS","difficulty": "Medium"}]'''
data = json.loads(json_string)

async def get_question_info(dialog_manager: DialogManager, **kwargs):
    victorina = Victorina(data[0])
    answers = victorina.get_answers()
    
    dialog_manager.dialog_data["correct_answer"] = victorina.get_correct_answer_key()
    
    return {
        'question': victorina.get_question(),
        'answers': list(answers.items()),
    }

async def on_answer_selected(callback, button, manager: DialogManager, item_id: str):
    user_answer = item_id
    correct_answer = manager.dialog_data.get("correct_answer")
    
    if (user_answer + "_correct" == correct_answer):
        await callback.answer("Правильно!")
    else:
        await callback.answer("Неверно!")
    
    manager.switch_to(GameSG.result)

game_window = Window(
    Format("❓ Вопрос:\n{question}"),
    
    Select(
        text=Format("{item[1]}"),
        id="answers_select",
        item_id_getter=lambda item: item[0],
        items="answers",
        on_click=on_answer_selected,
    ),
    
    Cancel(Const("⬅️ Выйти")),
    
    getter=get_question_info,
    state=GameSG.question
)