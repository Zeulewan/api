import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class APICallApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('API Call App')
        self.setGeometry(100, 100, 300, 200)

        self.result_label = QLabel('API response will appear here.')
        self.api_button = QPushButton('Make API Call')
        self.api_button.clicked.connect(self.make_api_call)

        layout = QVBoxLayout()
        layout.addWidget(self.api_button)
        layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def make_api_call(self):
        url = 'https://www.zeulewan.com/api.php'
        try:
            response = requests.get(url)
            data = response.json()
            self.result_label.setText(f'API Response: {data}')
        except Exception as e:
            self.result_label.setText(f'Error: {e}')

def main():
    app = QApplication(sys.argv)
    window = APICallApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
