from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow


class MainMenuBar:

    def __init__(self, window: QMainWindow):

        self.window = window

        self.menu_bar = window.menuBar()

        self._create_menus()

    def _create_menus(self):

        file_menu = self.menu_bar.addMenu("&File")
        edit_menu = self.menu_bar.addMenu("&Edit")
        view_menu = self.menu_bar.addMenu("&View")
        tools_menu = self.menu_bar.addMenu("&Tools")
        help_menu = self.menu_bar.addMenu("&Help")

        exit_action = QAction("E&xit", self.window)
        exit_action.triggered.connect(self.window.close)

        file_menu.addSeparator()
        file_menu.addAction(exit_action)