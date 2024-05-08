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
import psycopg2
import sys

class Face(QWidget):
	def __init__(self):
		super().__init__()
		self.cont()
		self.setFixedSize(320, 180)
		self.setWindowTitle('Авторизация')

		self.kc = QHBoxLayout()
		self.AUt = LogotBOX(self, self.conter, self.cur)

		self.btn = QPushButton('_проверка_\nСуществующие\n логины и пароли')
		self.btn.clicked.connect(self.Log_test)

		self.bnnexit = QPushButton('Закрыть', self)
		self.bnnexit.resize(50, 20)
		self.bnnexit.move(210, 140)
		self.bnnexit.clicked.connect(self.close)

		self.kc.addWidget(self.AUt)
		self.kc.addWidget(self.btn)
		self.setLayout(self.kc)

	def cont(self):
		password = '89105071534'
		self.conter = psycopg2.connect(
			database='postgress_intarface_db',
			user='postgres',
			password=password,
			host='127.0.0.1',
			port='')
		self.cur = self.conter.cursor()

	def Log_test(self):
		self.mess = QMessageBox()
		self.mess.setWindowTitle('Выберите проверяемое')
		self.mess.setText(' Проверяемое | Существующие логины и пароли внутри отдельного файла CSV. ')
		with open('CSVs/csv_user.csv', 'r', encoding='utf=8') as csvfile:
			file = csvfile.read().replace('\n', '\n\n').replace(',', ' | ')
			self.mess.setDetailedText(file)
		self.mess.show()
class LogotBOX(QWidget):
	def __init__(self, wg, conter, cur):
		self.wg = wg
		super().__init__(wg)
		self.conter = conter
		self.cur = cur

		self.laye = QVBoxLayout()

		self.occ_ = QLabel('Login')
		self.occ = QLineEdit(self)

		self.occ2_ = QLabel('Password')
		self.occ2 = QLineEdit(self)
		self.occ2.setEchoMode(QLineEdit.Password)

		self.bnn = QPushButton("Авторизироваться")
		self.bnn.clicked.connect(self.connecte)

		self.laye.addWidget(self.occ_)
		self.laye.addWidget(self.occ)
		self.laye.addWidget(self.occ2_)
		self.laye.addWidget(self.occ2)
		self.laye.addWidget(self.bnn)
		self.setLayout(self.laye)
	def sqlIns(self):
		logo, passw = self.occ.text(), self.occ2.text()
		self.cur.execute('select login, password '
						 'from user_table')
		self.users = self.cur.fetchall()
		for logo_passw in self.users:
			if logo == logo_passw[0] and int(passw) == logo_passw[1]:
				print(logo_passw)
				return True
		return False


	def connecte(self):
		print('Autorising...')
		if self.sqlIns():
			self.user = user_window()
			self.user.show()
		else:
			print('Неверные данные логина или пароля')
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