import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog


class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a vertical layout for the form
        layout = QVBoxLayout()

        # Create labels and input fields for HOST and PORT
        host_label = QLabel('Host:')
        self.host_input = QLineEdit()

        port_label = QLabel('Port:')
        self.port_input = QLineEdit()

        # Create a file chooser button
        file_button = QPushButton('Choose File')
        file_button.clicked.connect(self.choose_file)

        # Create a "Send" button
        send_button = QPushButton('Send')
        send_button.clicked.connect(self.send_data)

        # Add labels, input fields, and buttons to the layout
        layout.addWidget(host_label)
        layout.addWidget(self.host_input)
        layout.addWidget(port_label)
        layout.addWidget(self.port_input)
        layout.addWidget(file_button)
        layout.addWidget(send_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('PyQt Form with File Chooser')
        self.setGeometry(100, 100, 400, 200)

    def choose_file(self):
        # Open a file dialog to choose a file
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "All Files (*);;Text Files (*.txt)",
                                                   options=options)

        # Display the chosen file path in the host input field
        if file_path:
            self.host_input.setText(file_path)

    def send_data(self):
        # This function is called when the "Send" button is clicked
        host = self.host_input.text()
        port = self.port_input.text()

        # You can implement the code to send data to the specified host and port here
        print(f'Sending data to Host: {host}, Port: {port}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
