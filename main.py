import sys
from PyQt6.QtWidgets import QApplication
from layout import Website
app = QApplication(sys.argv)
window = Website()
window.show()
app.exec()