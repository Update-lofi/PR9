import sqlite3
from datetime import date

DATABASE = 'guestbook.db'

def get_db_connection():
    """Устанавливает соединение с базой данных"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к колонкам по имени (например, row['name'])
    return conn

def add_test_messages():
    """Временно добавляет тестовые данные в базу"""
    conn = get_db_connection()
    # Первое сообщение
    conn.execute(
        'INSERT INTO messages (name, message, created_at) VALUES (?, ?, ?)', 
        ('Анна', 'Отличный сайт!', '2026-05-28')
    )
    # Второе сообщение (дополненный код из Задания 3)
    conn.execute(
        'INSERT INTO messages (name, message, created_at) VALUES (?, ?, ?)', 
        ('Иван', 'Всем привет', '2026-05-27')
    )
    conn.commit()
    conn.close()

def init_db():
    """Создаёт таблицу messages, если её ещё нет"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
    # Задание 3: вызываем функцию добавления тестовых данных после создания таблицы
    # (В будущем эту строку нужно будет удалить или закомментировать)
    # add_test_messages()

def get_all_messages():
    """Возвращает все сообщения из таблицы, отсортированные от новых к старым"""
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY created_at DESC').fetchall()
    conn.close()
    return messages