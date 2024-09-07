# lexnlp/nlp_processor.py

import yaml
from .ollama_api import OllamaAPI
from .openai_api import OpenAIAPI
from .anthropic_api import AnthropicAPI

class NLPProcessor:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.ollama = OllamaAPI(config_path)
        self.openai = OpenAIAPI(config_path)
        self.anthropic = AnthropicAPI(config_path)

    def process_text(self, text, task, api='ollama', model=None):
        prompt = f"Perform the following NLP task on the given text: {task}\n\nText: {text}"
        
        if api == 'ollama':
            return self.ollama.generate_text(prompt, model)
        elif api == 'openai':
            return self.openai.generate_text(prompt)
        elif api == 'anthropic':
            return self.anthropic.generate_text(prompt)
        else:
            raise ValueError(f"Unsupported API: {api}")

if __name__ == "__main__":
    processor = NLPProcessor()
    text = "The quick brown fox jumps over the lazy dog."
    task = "Perform part-of-speech tagging on this sentence."
    result = processor.process_text(text, task, api='ollama', model='codellama')
    print(result)# lexnlp/nlp_processor.py

import yaml
import redis
import json
from .ollama_api import OllamaAPI
from .openai_api import OpenAIAPI
from .anthropic_api import AnthropicAPI
from .logger import nlp_logger

class NLPProcessor:
    def __init__(self, config_path='config.yaml'):
        try:
            with open(config_path, 'r') as file:
                self.config = yaml.safe_load(file)
            self.ollama = OllamaAPI(config_path)
            self.openai = OpenAIAPI(config_path)
            self.anthropic = AnthropicAPI(config_path)
            self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        except Exception as e:
            nlp_logger.error(f"Error initializing NLPProcessor: {str(e)}")
            raise

    def process_text(self, text, task, api='ollama', model=None):
        try:
            # Create a cache key
            cache_key = f"{api}:{model}:{task}:{text}"

            # Check if result is in cache
            cached_result = self.redis_client.get(cache_key)
            if cached_result:
                nlp_logger.info(f"Cache hit for key: {cache_key}")
                return json.loads(cached_result)

            prompt = f"Perform the following NLP task on the given text: {task}\n\nText: {text}"
            
            if api == 'ollama':
                result = self.ollama.generate_text(prompt, model)
            elif api == 'openai':
                result = self.openai.generate_text(prompt)
            elif api == 'anthropic':
                result = self.anthropic.generate_text(prompt)
            else:
                raise ValueError(f"Unsupported API: {api}")

            # Cache the result
            self.redis_client.setex(cache_key, 3600, json.dumps(result))  # Cache for 1 hour

            nlp_logger.info(f"Successfully processed text using {api} API")
            return result
        except Exception as e:
            nlp_logger.error(f"Error in process_text: {str(e)}")
            raise

if __name__ == "__main__":
    processor = NLPProcessor()
    text = "The quick brown fox jumps over the lazy dog."
    task = "Perform part-of-speech tagging on this sentence."
    result = processor.process_text(text, task, api='ollama', model='codellama')
    print(result)# lexnlp/nlp_processor.py

import yaml
from functools import lru_cache
from .ollama_api import OllamaAPI
from .openai_api import OpenAIAPI
from .anthropic_api import AnthropicAPI
from .logger import nlp_logger

class NLPProcessor:
    def __init__(self, config_path='config.yaml'):
        try:
            with open(config_path, 'r') as file:
                self.config = yaml.safe_load(file)
            self.ollama = OllamaAPI(config_path)
            self.openai = OpenAIAPI(config_path)
            self.anthropic = AnthropicAPI(config_path)
        except Exception as e:
            nlp_logger.error(f"Error initializing NLPProcessor: {str(e)}")
            raise

    @lru_cache(maxsize=100)
    def process_text(self, text, task, api='ollama', model=None):
        try:
            prompt = f"Perform the following NLP task on the given text: {task}\n\nText: {text}"
            
            if api == 'ollama':
                result = self.ollama.generate_text(prompt, model)
            elif api == 'openai':
                result = self.openai.generate_text(prompt)
            elif api == 'anthropic':
                result = self.anthropic.generate_text(prompt)
            else:
                raise ValueError(f"Unsupported API: {api}")

            nlp_logger.info(f"Successfully processed text using {api} API")
            return result
        except Exception as e:
            nlp_logger.error(f"Error in process_text: {str(e)}")
            raise

    def text_classification(self, text, categories):
        return self.process_text(text, f"Classify the following text into one of these categories: {', '.join(categories)}")

    def named_entity_recognition(self, text):
        return self.process_text(text, "Identify and list all named entities (e.g., person names, organizations, locations) in the following text:")

    def sentiment_analysis(self, text):
        return self.process_text(text, "Perform sentiment analysis on the following text and categorize it as positive, negative, or neutral:")

if __name__ == "__main__":
    processor = NLPProcessor()
    text = "The quick brown fox jumps over the lazy dog."
    result = processor.named_entity_recognition(text)
    print(result)# lexnlp/nlp_processor.py

import yaml
from functools import lru_cache
from .ollama_api import OllamaAPI
from .openai_api import OpenAIAPI
from .anthropic_api import AnthropicAPI
from .logger import nlp_logger

class NLPProcessor:
    def __init__(self, config_path='config.yaml'):
        try:
            with open(config_path, 'r') as file:
                self.config = yaml.safe_load(file)
            self.ollama = OllamaAPI(config_path)
            self.openai = OpenAIAPI(config_path)
            self.anthropic = AnthropicAPI(config_path)
        except Exception as e:
            nlp_logger.error(f"Error initializing NLPProcessor: {str(e)}")
            raise

    @lru_cache(maxsize=100)
    def process_text(self, text, task, api='ollama', model=None):
        try:
            prompt = f"Perform the following NLP task on the given text: {task}\n\nText: {text}"
            
            if api == 'ollama':
                result = self.ollama.generate_text(prompt, model)
            elif api == 'openai':
                result = self.openai.generate_text(prompt)
            elif api == 'anthropic':
                result = self.anthropic.generate_text(prompt)
            else:
                raise ValueError(f"Unsupported API: {api}")

            nlp_logger.info(f"Successfully processed text using {api} API")
            return result
        except Exception as e:
            nlp_logger.error(f"Error in process_text: {str(e)}")
            raise

    def text_classification(self, text, categories):
        return self.process_text(text, f"Classify the following text into one of these categories: {', '.join(categories)}")

    def named_entity_recognition(self, text):
        return self.process_text(text, "Identify and list all named entities (e.g., person names, organizations, locations) in the following text:")

    def sentiment_analysis(self, text):
        return self.process_text(text, "Perform sentiment analysis on the following text and categorize it as positive, negative, or neutral:")

if __name__ == "__main__":
    processor = NLPProcessor()
    text = "The quick brown fox jumps over the lazy dog."
    result = processor.named_entity_recognition(text)
    print(result)