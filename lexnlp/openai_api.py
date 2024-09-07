# lexnlp/openai_api.py

import openai
import yaml

class OpenAIAPI:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        openai.api_key = config['openai']['api_key']
        self.model = config['openai']['model']

    def generate_text(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']

if __name__ == "__main__":
    openai_api = OpenAIAPI()
    result = openai_api.generate_text("What is the capital of France?")
    print(result)