from flask import Flask, render_template
from database import init_db, get_all_messages

# Создаём экземпляр Flask-приложения
app = Flask(__name__)

# Инициализируем базу данных при запуске приложения
init_db()

# Определяем маршрут для главной страницы
@app.route('/')
def index():
    # Получаем все сообщения из базы данных
    messages = get_all_messages()
    
    # Отображаем HTML-шаблон и передаём в него переменную messages
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    # Запускаем встроенный веб-сервер Flask в режиме отладки
    app.run(debug=True)