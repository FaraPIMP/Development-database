# ui.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from database.database import get_all_employees, add_employee, update_employee, delete_employee
from reports.pdf_report import generate_pdf

class EmployeeManager(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Менеджер по работе с сотрудниками')
        self.setGeometry(100, 100, 800, 600)

        # Применяем стиль для всего интерфейса
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;                  /* Чёрный фон */
                color: #ffffff;                             /* Белый текст */
                font-family: 'DejaVu Sans', sans-serif;
            }
            QLineEdit, QTableWidget {
                background-color: #333333;                  /* Тёмно-серый фон для полей ввода и таблицы */
                color: #ffffff;
                border: 1px solid #ff4500;                  /* Красновато-оранжевая рамка */
            }
            QPushButton {
                background-color: #ff7f00;                  /* Оранжевый фон кнопок */
                color: #000000;                             /* Чёрный текст кнопок */
                border: 2px solid #ff0000;                  /* Красная граница */
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #ff4500;                  /* Насыщенный оранжево-красный фон при наведении */
            }
            QHeaderView::section {
                background-color: #ff7f00;                  /* Оранжевый фон заголовков таблицы */
                color: #000000;
                padding: 4px;
                border: 1px solid #ff0000;
            }
        """)

        self.layout = QVBoxLayout()
        
        self.form_layout = QFormLayout()
        
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.birth_date_input = QLineEdit()
        self.position_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.start_date_input = QLineEdit()

        self.form_layout.addRow('Имя:', self.first_name_input)
        self.form_layout.addRow('Фамилия:', self.last_name_input)
        self.form_layout.addRow('Дата рождения:', self.birth_date_input)
        self.form_layout.addRow('Должность:', self.position_input)
        self.form_layout.addRow('Телефон:', self.phone_input)
        self.form_layout.addRow('Электронная почта:', self.email_input)
        self.form_layout.addRow('Дата начала работы:', self.start_date_input)

        self.layout.addLayout(self.form_layout)
        
        # Кнопки
        self.add_button = QPushButton('Добавить сотрудника')
        self.update_button = QPushButton('Обновить информацию')
        self.delete_button = QPushButton('Удалить сотрудника')
        self.generate_report_button = QPushButton('Генерация отчета сотрудников в PDF')

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.generate_report_button)
        
        # Таблица сотрудников
        self.employee_table = QTableWidget()
        self.layout.addWidget(self.employee_table)

        # Привязка сигналов к слотам
        self.add_button.clicked.connect(self.add_employee)
        self.update_button.clicked.connect(self.update_employee)
        self.delete_button.clicked.connect(self.delete_employee)
        self.generate_report_button.clicked.connect(self.generate_report)

        self.load_employees()

        self.setLayout(self.layout)

    def load_employees(self):
        """Загрузка сотрудников в таблицу."""
        employees = get_all_employees()

        self.employee_table.setRowCount(len(employees))
        self.employee_table.setColumnCount(8)
        self.employee_table.setHorizontalHeaderLabels([
            'ID', 'Имя', 'Фамилия', 'Дата рождения', 'Должность', 
            'Телефон', 'Электронная почта', 'Дата начала работы'
        ])

        for row_num, row in enumerate(employees):
            for col_num, cell in enumerate(row):
                self.employee_table.setItem(row_num, col_num, QTableWidgetItem(str(cell)))

    def add_employee(self):
        """Добавить нового сотрудника."""
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        birth_date = self.birth_date_input.text()
        position = self.position_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        start_date = self.start_date_input.text()

        add_employee(first_name, last_name, birth_date, position, phone, email, start_date)
        self.load_employees()

    def update_employee(self):
        """Обновить данные сотрудника."""
        selected_row = self.employee_table.currentRow()
        if selected_row != -1:
            employee_id = self.employee_table.item(selected_row, 0).text()

            first_name = self.first_name_input.text()
            last_name = self.last_name_input.text()
            birth_date = self.birth_date_input.text()
            position = self.position_input.text()
            phone = self.phone_input.text()
            email = self.email_input.text()
            start_date = self.start_date_input.text()

            update_employee(employee_id, first_name, last_name, birth_date, position, phone, email, start_date)
            self.load_employees()

    def delete_employee(self):
        """Удалить сотрудника."""
        selected_row = self.employee_table.currentRow()
        if selected_row != -1:
            employee_id = self.employee_table.item(selected_row, 0).text()
            delete_employee(employee_id)
            self.load_employees()

    def generate_report(self):
        """Генерация отчета сотрудников в PDF."""
        try:
            generate_pdf()
            QMessageBox.information(self, 'Успех', 'Отчет успешно сгенерирован и сохранен как "employee_report.pdf".')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка при генерации отчета: {str(e)}')