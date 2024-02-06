import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QGraphicsView, QGraphicsScene, QWidget
from PyQt5.QtGui import QImage, QPixmap
import fitz  # PyMuPDF

class PDFViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Viewer')
        self.setGeometry(100, 100, 800, 600)

        # Central Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Graphics View
        self.graphics_view = QGraphicsView(self)
        layout.addWidget(self.graphics_view)

        # Graphics Scene
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.graphics_scene)

        # Open Button
        open_button = QPushButton('Open PDF', self)
        open_button.clicked.connect(self.openPDF)
        layout.addWidget(open_button)

    def openPDF(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        file_dialog.setViewMode(QFileDialog.Detail)

        file_path, _ = file_dialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")

        if file_path:
            self.showPDF(file_path)

    def showPDF(self, file_path):
        pdf_document = fitz.open(file_path)

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pixmap = page.get_pixmap()
            
            qt_image = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, QImage.Format_RGB32)

            pixmap = QPixmap.fromImage(qt_image)
            self.graphics_scene.addPixmap(pixmap)

        pdf_document.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_viewer = PDFViewerApp()
    pdf_viewer.show()
    sys.exit(app.exec_())
