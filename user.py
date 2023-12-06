import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        # Хеширование пароля перед сохранением в базу данных
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, database):
        # Регистрация пользователя в базе данных
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        values = (self.username, self.password)
        database.execute_query(query, values)
        database.commit()

    def login(self, database):
        # Проверка существования пользователя и сравнение хешей паролей
        query = "SELECT * FROM users WHERE username=? AND password=?"
        values = (self.username, self.password)
        database.execute_query(query, values)
        user_data = database.cursor.fetchone()

        if user_data:
            print("Авторизация успешна!")
        else:
            print("Ошибка авторизации. Проверьте правильность данных.")
