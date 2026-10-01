import psycopg2 
from PySide6.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow as Login 
from autorazation import Ui_MainWindow as Auto 

# Параметры подключения
conn = psycopg2.connect(
    dbname="db_pashka",      # имя базы данных
    user="postgres", # имя пользователя
    password="12345678",      # пароль
    host="localhost",       # хост (если сервер локальный)
    port="5432"              # порт (по умолчанию 5432)
)

# Дальше можно работать с базой через курсор
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

print(cursor.fetchall())

# Не забудьте закрыть соединение
cursor.close()
conn.close()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Login()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.go)
    def go(self):
        self.autoreraz = AutoReraz()
        self.autoreraz.show()

        self.close()


class AutoReraz(QMainWindow,):
    def __init__(self):
        super().__init__()

        self.ui = Auto()
        self.ui.setupUi(self)
        
def main():
    app = QApplication()
    window = LoginWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

