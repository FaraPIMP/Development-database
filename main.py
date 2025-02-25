import sys
import os
from PyQt5.QtWidgets import QApplication
from ui.ui import EmployeeManager
from database.database import create_db


def main():
    create_db()

    app = QApplication(sys.argv)
    window = EmployeeManager()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
