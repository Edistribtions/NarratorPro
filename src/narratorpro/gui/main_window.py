from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

from narratorpro.version import APP_NAME
from narratorpro.version import VERSION


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"{APP_NAME} {VERSION}")
        self.resize(1200, 800)

        central = QWidget()

        layout = QVBoxLayout()

        label = QLabel(
            "<h1>NarratorPro</h1>"
            "<p>Professional AI Narration Studio</p>"
        )

        label.setStyleSheet("font-size:18px;")
        label.setContentsMargins(30, 30, 30, 30)

        layout.addWidget(label)

        central.setLayout(layout)

        self.setCentralWidget(central)