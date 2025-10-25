from typing import Dict
import requests


class Victorina:
    def __init__(self, language='ru', category : str = None, difficulty : str = None):
        params = {
            'apiKey': 'ZC7HdPW3tEy7YlWIlBTZ7eueKScNNnOwOId0NDZA',
            'language': language,
            'limit': 1,
            'single_answer_only': 'true'
        }
        if category:
            params['category'] = category
        if difficulty:
            params['difficulty'] = difficulty
        
        self.url = "https://quizapi.io/api/v1/questions"
        try:
            response = requests.get(self.url, params=params)
            self.data = response.json()[0]
            
        except requests.exceptions.ConnectionError as e:
            print(f"Erorr: {e}")

    # def __init__(self, data):
    #     self.data = data

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

