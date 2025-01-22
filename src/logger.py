import logging
import os
from datetime import datetime

LOGFILE = F"{datetime.now().strftime("%m-%d-%Y-%H-%M-%S")}.log"
log_path = os.path.join(os.getcwd(),"logs",LOGFILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOGFILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ]  - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


if __name__ == "__main__":
    logging.info("logging has started.")