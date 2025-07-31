# نظام تسجيل لوج لجميع الرسائل والأخطاء
import logging

def setup_logger():
    logging.basicConfig(
        filename='arkon.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )