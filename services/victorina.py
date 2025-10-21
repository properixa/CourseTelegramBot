import requests
import json
from typing import Dict


json_string = '''[{"id": 5752,"question": "How do you use 'mapState' to access the state of a specific Vuex module?","description": "Learning how to map module state to component properties using 'mapState'.","answers": {"answer_a": "mapState(['stateProperty'])","answer_b": "mapState('moduleName', ['stateProperty'])","answer_c": "mapState('stateProperty')","answer_d": "mapState('moduleName/stateProperty')","answer_e": null,"answer_f": null},"multiple_correct_answers": "false","correct_answers": {"answer_a_correct": "false","answer_b_correct": "true","answer_c_correct": "false","answer_d_correct": "false","answer_e_correct": "false","answer_f_correct": "false"},"correct_answer": null,"explanation": "You use 'mapState('moduleName', ['stateProperty'])' to access and map a specific module's state properties to component properties.","tip": null,"tags": [{"name": "VueJS"}],"category": "VueJS","difficulty": "Medium"}]'''
data = json.loads(json_string)

class Victorina:
    # def __init__(self, language='ru', category : str = None, difficulty : str = None):
    #     params = {
    #         'apiKey': 'ZC7HdPW3tEy7YlWIlBTZ7eueKScNNnOwOId0NDZA',
    #         'language': language,
    #         'limit': 1,
    #         'single_answer_only': 'true'
    #     }
    #     if category:
    #         params['category'] = category
    #     if difficulty:
    #         params['difficulty'] = difficulty
        
    #     self.url = "https://quizapi.io/api/v1/questions"
    #     try:
    #         response = requests.get(self.url, params=params)
    #         self.data = response.json()[0]
            
    #     except requests.exceptions.ConnectionError as e:
    #         print(f"Erorr: {e}")

    def __init__(self, data):
        self.data = data

    def get_question(self) -> str:
        return self.data['question']

    
    def get_answers(self) -> Dict[str, str]:
        reuslt = {}
        for key, item in self.data['answers'].items():
            if item != None:
                reuslt[key] = item
        return reuslt
    
    def get_correct_answer_key(self) -> str:
        return [correct_answer for correct_answer in self.data['correct_answers'] if self.data['correct_answers'][correct_answer] == 'true'][0]

# victorina = Victorina(category="VueJS", difficulty="easy")
victorina = Victorina(data[0])
print(victorina.get_question())
print(victorina.get_answers())
print(victorina.get_correct_answer_key())
