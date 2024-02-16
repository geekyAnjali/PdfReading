import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from google.cloud import translate

class DictionaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English to Hindi Dictionary")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()
        self.translator = translate.TranslationServiceClient()

    def setup_ui(self):
        self.label = QLabel("Enter English word:")
        self.layout.addWidget(self.label)

        self.input_box = QLineEdit()
        self.layout.addWidget(self.input_box)

        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate)
        self.layout.addWidget(self.translate_button)

        self.translation_label = QLabel("")
        self.layout.addWidget(self.translation_label)

    def translate(self):
        word = self.input_box.text().lower()
        response = self.translator.translate_text(
            parent="845779094123/strange-vine-360311",
            contents=[word],
            target_language_code="hi"
        )
        hindi_meaning = response.translations[0].translated_text if response.translations else "Meaning not found"
        self.translation_label.setText(f"Hindi meaning: {hindi_meaning}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    sys.exit(app.exec_())
                                          