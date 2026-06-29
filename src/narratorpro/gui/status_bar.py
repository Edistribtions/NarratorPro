from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QStatusBar


class MainStatusBar:

    def __init__(self, window: QMainWindow):

        status = QStatusBar()

        status.showMessage("Ready")

        window.setStatusBar(status)