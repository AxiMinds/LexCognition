# lexnlp/anthropic_api.py

import anthropic
import yaml

class AnthropicAPI:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.client = anthropic.Client(api_key=config['anthropic']['api_key'])
        self.model = config['anthropic']['model']

    def generate_text(self, prompt):
        response = self.client.completion(
            model=self.model,
            prompt=f"Human: {prompt}\n\nAssistant:",
            max_tokens_to_sample=300
        )
        return response.completion

if __name__ == "__main__":
    anthropic_api = AnthropicAPI()
    result = anthropic_api.generate_text("What is the capital of France?")
    print(result)