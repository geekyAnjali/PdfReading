import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QAction, QFileDialog, QFontDialog, QColorDialog
from PyQt5.QtGui import QFont, QColor, QTextCursor,QTextDocument
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog
import fitz 

class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 800, 600)

        self.textEdit = QTextEdit()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.textEdit)

        # Button Layout
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Save Button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_file)
        button_layout.addWidget(save_button)

        # Save as PDF Button
        pdf_button = QPushButton("Save as PDF")
        pdf_button.clicked.connect(self.save_as_pdf)
        button_layout.addWidget(pdf_button)

        load_pdf_button = QPushButton("Load PDF File")
        load_pdf_button.clicked.connect(self.load_pdf)
        layout.addWidget(load_pdf_button)
        # Font Style Button
        font_button = QPushButton("Font Style")
        font_button.clicked.connect(self.set_font)
        button_layout.addWidget(font_button)

        # Bold Button
        bold_button = QPushButton("Bold")
        bold_button.clicked.connect(self.set_bold)
        button_layout.addWidget(bold_button)

        # Italic Button
        italic_button = QPushButton("Italic")
        italic_button.clicked.connect(self.set_italic)
        button_layout.addWidget(italic_button)

        # Underline Button
        underline_button = QPushButton("Underline")
        underline_button.clicked.connect(self.set_underline)
        button_layout.addWidget(underline_button)

        # Headings Button
        headings_button = QPushButton("Headings")
        headings_button.clicked.connect(self.set_headings)
        button_layout.addWidget(headings_button)

        # Color Button
        color_button = QPushButton("Color")
        color_button.clicked.connect(self.set_color)
        button_layout.addWidget(color_button)
        
        font_button.clicked.connect(self.set_font)
        # layout.addWidget(font_button)

    def set_default_font(self):
        default_font = QFont("Arial", 12)  # Default font: Arial, size 12
        self.textEdit.setFont(default_font)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textEdit.toPlainText())

    def save_as_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save as PDF", "", "PDF Files (*.pdf)")
        if file_path:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_path)
            self.textEdit.document().print_(printer)

    def set_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def set_bold(self):
        if self.textEdit.fontWeight() != QFont.Bold:
            self.textEdit.setFontWeight(QFont.Bold)
        else:
            self.textEdit.setFontWeight(QFont.Normal)

    def set_italic(self):
        self.textEdit.setFontItalic(not self.textEdit.fontItalic())

    def set_underline(self):
        self.textEdit.setFontUnderline(not self.textEdit.fontUnderline())

    def set_headings(self):
        current_font = self.textEdit.font()
        current_font.setPointSize(16)
        self.textEdit.setFont(current_font)

    def set_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)
            

    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if file_path:
            doc = fitz.open(file_path)
            text_with_format = ""
            for page in doc:
                for block in page.get_text("dict")["blocks"]:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            font_size = span["size"]
                            font_color = QColor.fromRgb(span["color"][0], span["color"][1], span["color"][2])
                            font_name = span["font"]
                            text_with_format += f'<span style="font-family:{font_name}; font-size:{font_size}pt; color:rgb({font_color.red()},{font_color.green()},{font_color.blue()})">{span["text"]}</span>'
                text_with_format += "<br>"
            self.textEdit.setHtml(text_with_format)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    text_editor = TextEditor()
    text_editor.show()
    sys.exit(app.exec_())
