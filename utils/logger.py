from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO")
logger.add("logs/test_{time:YYYYMMDD_HHmmss}.log", rotation="10 MB")
