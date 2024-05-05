from PyQt5.QtWidgets import(
QApplication,
QWidget,
QPushButton,
QTableWidgetItem,
QMainWindow,
QTableWidget,
QLineEdit,
QLabel,
QVBoxLayout
)
import sys

class Face(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 300, 400)
		self.setWindowTitle('Приложение')

		self.laye = QVBoxLayout()
		self.txtA = QLabel('AAAAAAAAAA')
		self.laye.addWidget(self.txtA)
		self.setLayout(self.laye)

		self.bnn = QPushButton("Авторизироваться", self)
		self.bnn.resize(110, 25)
		self.bnn.move(70, 300)
		self.bnn.clicked

		self.occ = QLineEdit(self)
		self.occ.resize(160, 25)
		self.occ.move(70, 200)

		self.occ2 = QLineEdit(self)
		self.occ2.resize(160, 25)
		self.occ2.move(70, 250)




ppp = QApplication(sys.argv)
exe = Face()
exe.show()
sys.exit(ppp.exec_())