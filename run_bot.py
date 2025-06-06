
#!/usr/bin/env python3
"""
Простой запуск бота ScamHelper
"""

import os
import sys

def main():
    # Проверяем токен
    if not os.getenv('TELEGRAM_BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN') == 'YOUR_BOT_TOKEN_HERE':
        print("❌ Установите TELEGRAM_BOT_TOKEN в переменные окружения!")
        sys.exit(1)
    
    try:
        # Инициализируем БД
        print("🔄 Инициализация базы данных...")
        import init_db
        init_db.init_database()
        
        # Запускаем бота
        print("🚀 Запуск бота...")
        import scamhelper
        scamhelper.bot.polling(none_stop=True, interval=0)
        
    except KeyboardInterrupt:
        print("\n⏹️  Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
