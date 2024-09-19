import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class PDFViewerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None,pdf_path=None):
        super().__init__(parent)
        self.pdf_path = pdf_path
        self.setup_ui()

    def setup_ui(self):   
        layout = QtWidgets.QVBoxLayout(self)
        self.webview = QtWebEngineWidgets.QWebEngineView()
        layout.addWidget(self.webview)
        layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        layout.setSpacing(0)  # Set spacing to zero
        self.webview.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.webview.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.load_pdf(self.pdf_path)

    def load_pdf(self,path):
        self.pdf_path = path 
        self.webview.load(QtCore.QUrl.fromUserInput(self.pdf_path))

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    pdf_path = r"c:\Users\pk\Downloads\Study material Pdfs\let-us-python-3nbsped.pdf"
    window = PDFViewerWidget(pdf_path=pdf_path)
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())
