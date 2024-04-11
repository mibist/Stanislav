import requests as rq
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def clean_logs():
    # Очистка логов перед записью
    log_files = ['success_responses.log', 'bad_responses.log', 'blocked_responses.log']
    for log_file in log_files:
        with open(log_file, 'w'):
            pass

clean_logs()

# Создаем логгеры для каждого типа ответов
success_logger = logging.getLogger('SuccessLogger')
success_logger.setLevel(logging.INFO)
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_formatter = logging.Formatter('%(levelname)s: %(message)s')
success_handler.setFormatter(success_formatter)
success_logger.addHandler(success_handler)

bad_logger = logging.getLogger('BadLogger')
bad_logger.setLevel(logging.WARNING)
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.WARNING)
bad_formatter = logging.Formatter('%(levelname)s: %(message)s')
bad_handler.setFormatter(bad_formatter)
bad_logger.addHandler(bad_handler)

blocked_logger = logging.getLogger('BlockedLogger')
blocked_logger.setLevel(logging.ERROR)
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.ERROR)
blocked_formatter = logging.Formatter('%(levelname)s: %(message)s')
blocked_handler.setFormatter(blocked_formatter)
blocked_logger.addHandler(blocked_handler)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            success_logger.info(f"{site}, response - {response.status_code}")
        else:
            bad_logger.warning(f"{site}, response - {response.status_code}")
    except rq.exceptions.RequestException as e:
        blocked_logger.error(f"{site}, NO CONNECTION")