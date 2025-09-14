import logging
import os
from logging.handlers import RotatingFileHandler
from from_root.root import from_root
from datetime import datetime

# Hằng số cho cấu hình nhật ký
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Xây dựng đường dẫn tệp nhật ký
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
Định cấu hình ghi nhật ký với trình xử lý tệp xoay và trình xử lý bảng điều khiển.
    """
    # Tạo một bộ ghi nhật ký tùy chỉnh
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    #Xác định định dạng
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # Trình xử lý tập tin với vòng quay
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    #Người xử lý console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Thêm trình xử lý vào logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Định cấu hình logger
configure_logger()