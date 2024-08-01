import os ,sys,logging


logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"

log_filepath=os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath),# it gives log in log folder 
              logging.StreamHandler(sys.stdout)]#it gives log info on terminal 
)

logger=logging.getLogger("mlProjectLogger")