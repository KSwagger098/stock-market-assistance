"""
This module is used to provide tokens to other modules.
"""

import os

from dotenv import find_dotenv, load_dotenv

def give_token(variable_name: str) -> str:
    """
    Given the variable name, returns a token relative to the variable name
    """
    env_path = find_dotenv()
    load_dotenv(env_path)
    return os.getenv(variable_name)

