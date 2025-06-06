
#!/usr/bin/env python3
"""
Простой запуск бота ScamHelper
"""

import os
import sys

def main():
    # Проверяем токен
    if not os.getenv('TELEGRAM_BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN') == 'YOUR_BOT_TOKEN_HERE':
        sys.exit(1)
    
    try:
        # Инициализируем БД
        import init_db
        init_db.init_database()
        
        # Запускаем бота
        import scamhelper
        scamhelper.bot.polling(none_stop=True, interval=0)
        
    except KeyboardInterrupt:
        pass
    except Exception as e:
        sys.exit(1)

if __name__ == "__main__":
    main()
