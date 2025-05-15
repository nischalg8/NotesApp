import logging
import os

# absolute path for finding logging.ini
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGING_CONFIG_PATH = os.path.join(BASE_DIR, "..", "logging.ini")
LOGGING_CONFIG_PATH = os.path.abspath(LOGGING_CONFIG_PATH)

logger = logging.getLogger(__name__)