import os
import logging
import platform
import multiprocessing
from modules.logering import setup_logger


# number of cores
cores = multiprocessing.cpu_count()

# operating system
system = platform.system()

# root data_path
root_path = os.path.dirname(os.path.realpath(__file__))

# seed
seed = 42

# logging
log_level = logging.INFO
log_name = os.path.join(root_path, "log.log")
logger = setup_logger("logger", log_name, log_level)