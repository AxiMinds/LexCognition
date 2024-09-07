# lexnlp/ollama_api.py

import requests
import yaml

class OllamaAPI:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.base_url = f"{config['ollama']['server']}:{config['ollama']['port']}"
        self.models = config['ollama']['models']
        self.default_model = config['default_model']

    def generate_text(self, prompt, model_name=None):
        if model_name is None:
            model_name = self.default_model
        
        model_config = next((m for m in self.models if m['name'] == model_name), None)
        if not model_config:
            raise ValueError(f"Model {model_name} not found in configuration.")

        system_prompt = model_config['system_prompt']
        
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": model_name,
                "prompt": f"{system_prompt}\n\nHuman: {prompt}\n\nAssistant:",
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()['response']

if __name__ == "__main__":
    ollama = OllamaAPI()
    result = ollama.generate_text("What is the capital of France?")
    print(result)# lexnlp/ollama_api.py

import requests
import yaml
from .logger import ollama_logger

class OllamaAPI:
    def __init__(self, config_path='config.yaml'):
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            self.base_url = f"{config['ollama']['server']}:{config['ollama']['port']}"
            self.models = config['ollama']['models']
            self.default_model = config['default_model']
        except Exception as e:
            ollama_logger.error(f"Error initializing OllamaAPI: {str(e)}")
            raise

    def generate_text(self, prompt, model_name=None):
        try:
            if model_name is None:
                model_name = self.default_model
            
            model_config = next((m for m in self.models if m['name'] == model_name), None)
            if not model_config:
                raise ValueError(f"Model {model_name} not found in configuration.")

            system_prompt = model_config['system_prompt']
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": model_name,
                    "prompt": f"{system_prompt}\n\nHuman: {prompt}\n\nAssistant:",
                    "stream": False
                }
            )
            response.raise_for_status()
            ollama_logger.info(f"Successfully generated text using model {model_name}")
            return response.json()['response']
        except requests.RequestException as e:
            ollama_logger.error(f"Error calling Ollama API: {str(e)}")
            raise
        except Exception as e:
            ollama_logger.error(f"Unexpected error in generate_text: {str(e)}")
            raise

if __name__ == "__main__":
    ollama = OllamaAPI()
    result = ollama.generate_text("What is the capital of France?")
    print(result)