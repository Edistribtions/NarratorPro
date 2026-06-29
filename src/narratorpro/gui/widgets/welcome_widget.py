from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class WelcomeWidget(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("NarratorPro")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
        """)

        subtitle = QLabel("Professional AI Narration Studio")

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            font-size:16px;
            color:gray;
        """)

        layout.addStretch()

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addStretch()

        self.setLayout(layout)