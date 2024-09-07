# lexnlp/logger.py

import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup loggers
ollama_logger = setup_logger('ollama', 'logs/ollama.log')
openai_logger = setup_logger('openai', 'logs/openai.log')
anthropic_logger = setup_logger('anthropic', 'logs/anthropic.log')
nlp_logger = setup_logger('nlp', 'logs/nlp.log')