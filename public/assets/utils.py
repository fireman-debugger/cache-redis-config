import logging
import os
from configparser import ConfigParser
from typing import Dict

__all__ = ['load_config', 'get_env_var']

def load_config(file_path: str) -> Dict[str, str]:
    """
    Load configuration from a file.
    
    Args:
    file_path (str): Path to the configuration file.
    
    Returns:
    Dict[str, str]: Configuration dictionary.
    """
    config = ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}

def get_env_var(var_name: str, default: str = None) -> str:
    """
    Get environment variable.
    
    Args:
    var_name (str): Environment variable name.
    default (str, optional): Default value if variable is not set. Defaults to None.
    
    Returns:
    str: Environment variable value or default value if not set.
    """
    return os.environ.get(var_name, default) if default else os.environ.get(var_name)

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up logger.
    
    Args:
    name (str): Logger name.
    level (int, optional): Logger level. Defaults to logging.INFO.
    
    Returns:
    logging.Logger: Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger