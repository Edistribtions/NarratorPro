from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QToolBar


class MainToolBar:

    def __init__(self, window: QMainWindow):

        toolbar = QToolBar("Main Toolbar")

        toolbar.setMovable(False)

        toolbar.setFloatable(False)

        window.addToolBar(Qt.TopToolBarArea, toolbar)