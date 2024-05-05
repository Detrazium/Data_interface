from PyQt5.QtWidgets import(
QApplication,
QWidget,
QPushButton,
QTableWidgetItem,
QMainWindow,
QTableWidget,
QLineEdit,
QLabel,

QVBoxLayout,
QHBoxLayout,
)
import sys

class Face(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(320, 200)
		# self.setGeometry(50, 100, 300, 100)
		self.setWindowTitle('Приложение')

		self.kc = QHBoxLayout()
		self.AUt = LogotBOX(self)
		self.btn = QPushButton('Существующие\n логины и пароли')

		self.kc.addWidget(self.AUt)
		self.kc.addWidget(self.btn)
		self.setLayout(self.kc)


class LogotBOX(QWidget):
	def __init__(self, wg):
		self.wg = wg
		super().__init__(wg)
		self.setGeometry(50, 50, 150, 300)

		self.laye = QVBoxLayout()

		self.bnn = QPushButton("Авторизироваться")

		self.occ_ = QLabel('Login')
		self.occ = QLineEdit(self)

		self.occ2_ = QLabel('Password')
		self.occ2 = QLineEdit(self)


		self.laye.addWidget(self.occ_)
		self.laye.addWidget(self.occ)
		self.laye.addWidget(self.occ2_)
		self.laye.addWidget(self.occ2)
		self.laye.addWidget(self.bnn)
		self.setLayout(self.laye)


ppp = QApplication(sys.argv)
exe = Face()
exe.show()
sys.exit(ppp.exec_())