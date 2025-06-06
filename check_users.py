
import scamhelper_database as db

def check_user_count():
    try:
        count = db.users_db()
        print(f"Количество пользователей в боте: {count}")
        return count
    except Exception as e:
        print(f"Ошибка при получении количества пользователей: {e}")
        return 0

if __name__ == "__main__":
    check_user_count()
