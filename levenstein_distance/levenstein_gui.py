from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QGridLayout
from levenstein import levenstein
import sys

class LevensteinGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Levenstein's distance")
        self.text1 = QLineEdit()
        self.text2 = QLineEdit()
        text_title = QLabel("Words:")

        button = QPushButton("Calculate Levenstein's distance")
        self.result = QLabel()
        result_title = QLabel("Result:")

        button.clicked.connect(self.calculate_levenstein)

        layout = QGridLayout()
        layout.addWidget(self.text1, 0, 1)
        layout.addWidget(self.text2, 1, 1)
        layout.addWidget(text_title, 0, 0, 2, 1)
        layout.addWidget(button, 2, 1)
        layout.addWidget(result_title, 3, 0)
        layout.addWidget(self.result, 3, 1)

        self.setLayout(layout)
        self.show()

    def calculate_levenstein(self):
        a = self.text1.text()
        b = self.text2.text()
        self.result.setText(str(levenstein(a, b)))
        self.result.adjustSize()

def run():
    app = QApplication([])
    app.setStyle("Fusion")
    window = LevensteinGUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
