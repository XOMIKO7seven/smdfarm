
#!/usr/bin/env python3
"""
Простой запуск бота ScamHelper с автоперезапуском
"""

import os
import sys
import time

def main():
    max_retries = 5
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Проверяем токен
            if not os.getenv('TELEGRAM_BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN') == 'YOUR_BOT_TOKEN_HERE':
                sys.exit(1)
            
            # Инициализируем БД
            import init_db
            init_db.init_database()
            
            # Запускаем бота
            import scamhelper
            scamhelper.bot.polling(none_stop=True, interval=0)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(min(60, 10 * retry_count))  # Экспоненциальная задержка
                continue
            else:
                sys.exit(1)

if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            time.sleep(30)  # Ждем 30 секунд перед полным перезапуском
            continue
