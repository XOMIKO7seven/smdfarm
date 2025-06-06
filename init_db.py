
import sqlite3

def init_database():
    """Initialize the SQLite database with users table"""
    try:
        with sqlite3.connect("evidence.db") as con:
            cur = con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    date TEXT,
                    warning INTEGER DEFAULT 0
                )
            ''')
            con.commit()
            print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

if __name__ == "__main__":
    init_database()
