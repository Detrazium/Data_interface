from PyQt5.QtWidgets import(
QApplication,
QWidget,
QPushButton,
QTableWidgetItem,
QMainWindow,
QTableWidget,
QLineEdit,
QLabel,
QMessageBox,

QVBoxLayout,
QHBoxLayout,
)
import sys

class Face(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(320, 200)
		self.setWindowTitle('Приложение')

		self.kc = QHBoxLayout()
		self.AUt = LogotBOX(self)
		self.btn = QPushButton('_проверка_\nСуществующие\n логины и пароли')
		self.btn.clicked.connect(self.Log_test)

		self.kc.addWidget(self.AUt)
		self.kc.addWidget(self.btn)
		self.setLayout(self.kc)

	def Log_test(self):
		self.mess = QMessageBox()
		self.mess.setWindowTitle('Выберите проверяемое')
		self.mess.setText(' Проверяемое | Существующие логины и пароли внутри отдельного файла CSV. ')
		with open('CSVs/csv_user.csv', 'r', encoding='utf=8') as csvfile:
			file = csvfile.read().replace('\n', '\n\n').replace(',', ' | ')
			self.mess.setDetailedText(file)
		self.mess.show()
class LogotBOX(QWidget):
	def __init__(self, wg):
		self.wg = wg
		super().__init__(wg)
		self.laye = QVBoxLayout()

		self.bnn = QPushButton("Авторизироваться")
		self.bnn.clicked.connect(self.connecte)

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
	def connecte(self):
		print('Autorising...')
		self.wg.close()

		self.user = user_window()
		self.user.show()
class user_window(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(500, 500)
		self.cont = QVBoxLayout()





		self.inn = windowInfo(self)
		self.cont.addWidget(self.inn)
		self.setLayout(self.cont)
class windowInfo(QWidget):
	def __init__(self,wg):
		self.wg = wg
		super().__init__(wg)
		self.laye = QHBoxLayout()

		self.btn = QPushButton('exit')
		self.btn.clicked.connect(self.closed)





		self.laye.addWidget(self.btn)
		self.setLayout(self.laye)
	def closed(self):
		print('close')
		self.wg.close()
ppp = QApplication(sys.argv)
exe = Face()
exe.show()
sys.exit(ppp.exec_())