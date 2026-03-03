from app import create_app

# Создаем экземпляр приложения
app = create_app()

if __name__ == '__main__':
    # Запускаем встроенный сервер Flask
    app.run(
        host='0.0.0.0',  # локальный хост
        port=5000,          # стандартный порт Flask
        debug=True          # режим отладки (авто-перезагрузка)
    )