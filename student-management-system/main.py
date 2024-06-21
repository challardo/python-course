from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QVBoxLayout,
    QComboBox,
)
from PyQt6.QtGui import QAction
import sys
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        # self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(
                    row_number, column_number, QTableWidgetItem(str(data))
                )
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.student_name_edit = QLineEdit()
        self.student_name_edit.setPlaceholderText("Name")
        layout.addWidget(self.student_name_edit)

        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Physics", "Astronomy"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile_name_edit = QLineEdit()
        self.mobile_name_edit.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile_name_edit)

        button = QPushButton("Create")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name_edit.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_name_edit.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name,course,mobile) VALUES (?,?,?)",
            (
                name,
                course,
                mobile,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
