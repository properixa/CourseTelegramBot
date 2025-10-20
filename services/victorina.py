import requests
import json

#url = "https://quizapi.io/api/v1/questions?apiKey=ZC7HdPW3tEy7YlWIlBTZ7eueKScNNnOwOId0NDZA&limit=1&multiple_correct_answers=false"
#response = requests.get(url)
#data = response.json()
json_string = '''[{"id": 5752,"question": "How do you use 'mapState' to access the state of a specific Vuex module?","description": "Learning how to map module state to component properties using 'mapState'.","answers": {"answer_a": "mapState(['stateProperty'])","answer_b": "mapState('moduleName', ['stateProperty'])","answer_c": "mapState('stateProperty')","answer_d": "mapState('moduleName/stateProperty')","answer_e": null,"answer_f": null},"multiple_correct_answers": "false","correct_answers": {"answer_a_correct": "false","answer_b_correct": "true","answer_c_correct": "false","answer_d_correct": "false","answer_e_correct": "false","answer_f_correct": "false"},"correct_answer": null,"explanation": "You use 'mapState('moduleName', ['stateProperty'])' to access and map a specific module's state properties to component properties.","tip": null,"tags": [{"name": "VueJS"}],"category": "VueJS","difficulty": "Medium"}]'''
data = json.loads(json_string)
print(data[0])

class Victorina:
    pass
