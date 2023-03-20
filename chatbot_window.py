from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton
from chatbot import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    """
    Graphical user interface for the chatbot app
    """
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)

        self.chatbot = Chatbot()

        # Add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        """
        Send the user's input to the chatbot api
        :return: None
        """
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333'>Me: {user_input}</p?")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        """
        Gets a response from the chatbot based on the user's input
        :param user_input: the text entered by the user into the input field
        :return: None
        """
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333'>Chatbot: {response}</p>")
