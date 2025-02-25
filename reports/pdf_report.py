# pdf_report.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from database.database import get_all_employees

# Регистрируем шрифты, поддерживающие кириллицу
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf'))

def generate_pdf():
    # Получаем данные сотрудников из базы
    employees = get_all_employees()
    
    # Формируем данные для таблицы: первая строка – заголовки, далее данные сотрудников
    data = [
        ['ID', 'Имя', 'Фамилия', 'Дата рождения', 'Должность', 'Телефон', 'Почта', 'Дата начала работы']
    ]
    
    for emp in employees:
        # Преобразуем все элементы в строки для корректного отображения
        data.append([str(item) for item in emp])
    
    # Создаем PDF документ
    pdf_file = "employee_report.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    
    # Создаем таблицу
    table = Table(data)
    
    # Определяем стиль таблицы
    style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),           # Используем DejaVuSans для всей таблицы
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),         # Фон заголовков
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),               # Сетка таблицы
        ('FONTNAME', (0, 0), (-1, 0), 'DejaVuSans-Bold'),          # Жирный шрифт для заголовков
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),                     # Выравнивание по центру
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ])
    
    table.setStyle(style)
    
    # Строим PDF документ
    elements = [table]
    doc.build(elements)
