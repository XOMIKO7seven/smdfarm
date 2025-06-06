
#!/usr/bin/env python3
"""
ScamHelper Bot Launcher
Основной файл для запуска Telegram бота с обработкой ошибок и логированием
"""

import os
import sys
import time
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def check_environment():
    """Проверяет наличие необходимых переменных окружения"""
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not bot_token or bot_token == 'YOUR_BOT_TOKEN_HERE':
        logger.error("❌ TELEGRAM_BOT_TOKEN не установлен!")
        logger.info("💡 Установите токен бота в переменные окружения")
        return False
    return True

def initialize_database():
    """Инициализирует базу данных"""
    try:
        logger.info("🔄 Инициализация базы данных...")
        import init_db
        init_db.init_database()
        logger.info("✅ База данных успешно инициализирована")
        return True
    except Exception as e:
        logger.error(f"❌ Ошибка инициализации базы данных: {e}")
        return False

def start_bot():
    """Запускает бота"""
    try:
        logger.info("🚀 Запуск ScamHelper бота...")
        
        # Импортируем модули бота
        import scamhelper
        
        logger.info("✅ Бот успешно запущен!")
        logger.info("📢 Бот готов к работе...")
        
        # Запускаем бота
        scamhelper.bot.polling(none_stop=True, interval=0)
        
    except KeyboardInterrupt:
        logger.info("⏹️  Бот остановлен пользователем")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
        return False

def main():
    """Основная функция запуска"""
    print("=" * 50)
    print("🤖 ScamHelper Bot Launcher")
    print(f"📅 Запуск: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Проверяем переменные окружения
    if not check_environment():
        logger.error("💥 Не удалось запустить бота из-за отсутствия токена")
        sys.exit(1)
    
    # Инициализируем базу данных
    if not initialize_database():
        logger.error("💥 Не удалось инициализировать базу данных")
        sys.exit(1)
    
    # Запускаем бота с автоперезапуском при ошибках
    max_retries = 5
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            start_bot()
            break
        except Exception as e:
            retry_count += 1
            logger.error(f"❌ Попытка {retry_count}/{max_retries} неудачна: {e}")
            
            if retry_count < max_retries:
                wait_time = min(60, 10 * retry_count)  # Экспоненциальная задержка
                logger.info(f"⏳ Повторный запуск через {wait_time} секунд...")
                time.sleep(wait_time)
            else:
                logger.error("💥 Превышено максимальное количество попыток запуска")
                sys.exit(1)

if __name__ == "__main__":
    main()
