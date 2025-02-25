import sqlite3
import os
DB_PATH = "C:/Users/sdas4/Desktop/dz2/Development-database/database/employee_management.db"

if not os.path.exists(DB_PATH):
    print("Ошибка: База данных не найдена. Поместите файл employee_management.db в папку database.")
else:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    print("База данных успешно подключена.")


def create_db():
    """Создание базы данных и таблицы сотрудников."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_date DATE,
        position TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        start_date DATE
    )
    ''')
    conn.commit()
    conn.close()

def get_all_employees():
    """Получить всех сотрудников."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def add_employee(first_name, last_name, birth_date, position, phone, email, start_date):
    """Добавить сотрудника в базу данных."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO employees (first_name, last_name, birth_date, position, phone, email, start_date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, birth_date, position, phone, email, start_date))
    conn.commit()
    conn.close()

def update_employee(employee_id, first_name, last_name, birth_date, position, phone, email, start_date):
    """Обновить данные сотрудника."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE employees
    SET first_name = ?, last_name = ?, birth_date = ?, position = ?, phone = ?, email = ?, start_date = ?
    WHERE id = ?
    ''', (first_name, last_name, birth_date, position, phone, email, start_date, employee_id))
    conn.commit()
    conn.close()

def delete_employee(employee_id):
    """Удалить сотрудника из базы данных."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    conn.commit()
    conn.close()
