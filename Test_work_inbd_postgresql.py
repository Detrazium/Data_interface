from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush

from PyQt5.QtWidgets import(
QApplication,
QWidget,
QPushButton,

QComboBox,
QTableWidgetItem,

QTableWidget,
QLineEdit,
QLabel,
QMessageBox,
QTableWidgetSelectionRange,

QVBoxLayout,
QHBoxLayout,
)
import psycopg2
import sys
from No_import_file import password

class Face(QWidget):
	"""Окно авторизации"""
	def __init__(self):
		super().__init__()
		self.cont()
		self.setFixedSize(320, 180)
		self.setWindowTitle('Авторизация')

		self.kc = QHBoxLayout()
		self.AUt = LogotBOX(self)

		self.btn = QPushButton('_проверка_\nСуществующие\n логины и пароли')
		self.btn.clicked.connect(self.Log_test)

		self.bnnexit = QPushButton('Закрыть', self)
		self.bnnexit.resize(50, 20)
		self.bnnexit.move(210, 140)
		self.bnnexit.clicked.connect(self.close)
		self.bnnexit.clicked.connect(self.conter.close)

		self.kc.addWidget(self.AUt)
		self.kc.addWidget(self.btn)
		self.setLayout(self.kc)

	def cont(self):
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
			file = csvfile.read().replace('\n', '\n\n').replace(',', '|')
			self.mess.setDetailedText(file)
		self.mess.show()
class LogotBOX(QWidget):
	def __init__(self, wg):
		self.wg = wg
		super().__init__(wg)

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
		self.logo, self.pas = self.occ.text(), self.occ2.text()
		if self.pas.isdigit():
			self.wg.cur.execute(f"select exists (select * from user_table where login = '{self.logo}');")
			self.log = self.wg.cur.fetchall()

			self.wg.cur.execute(f"select exists (select * from user_table where password = '{self.pas}')")
			self.passw = self.wg.cur.fetchall()

			check = [*self.log[0], *self.passw[0]]
			if False not in check:
				return True
			return False
		else:
			print('lol')
			return False


	def connecte(self):
		print('Autorising...')
		if self.sqlIns():
			user = user_window(self.logo)
			user.show()
			self.wg.close()
		else:
			print('Неверные данные логина или пароля')
class user_window(QWidget):
	"""Окно пользователя"""
	def __init__(self, user):
		self.user = user
		super().__init__()
		self.conted()
		self.setWindowTitle('Окно пользователя')
		self.setFixedSize(1020, 400)
		self.cont = QHBoxLayout()

		self.get_logo_name()
		self.btns = Usp(self)

		self.inn = wIn(self, self.key)

		self.StatusComp()
		self.clientId()

		self.cont.addWidget(self.btns)
		self.cont.addWidget(self.inn)
		self.setLayout(self.cont)
	def clientId(self):

		self.Cli = QLabel('id_account', self)
		self.Cli.move(50, 50)

		self.CliL = QLineEdit(self)
		self.CliL.move(50, 85)
		self.CliL.resize(120, 23)

		self.CliEdit = QPushButton('Изменить Статус', self)
		self.CliEdit.clicked.connect(self.getIt)
		self.CliEdit.clicked.connect(self.correctinDB)

		self.CliEdit.move(50, 155)
		self.CliEdit.resize(100, 23)
	def getIt(self):
		self.id = self.CliL.text()
		self.statuss = self.bCb.currentText()

		tkey = self.inn.findItems(self.id, Qt.MatchContains)
		rows = []
		for el in tkey:
			if el.column() == 0:
				ss = self.inn.item(el.row(), 0)
				if ss.text() == self.id:
					for ell in range(0, 8):
						elrow = self.inn.item(el.row(), ell)
						rows.append(elrow.text())
					rows.append(el.row())
					self.status = QTableWidgetItem(self.statuss)
					self.inn.setItem(el.row()+1, -1, self.status)
	def correctinDB(self):
		self.cur.execute(f"""
			UPDATE client_table 
			SET status = '{self.statuss}' 
			WHERE id_accounts = '{self.id}'""")
		self.conter.commit()


	def StatusComp(self):
		self.bCb = QComboBox(self)
		self.bCb.setGeometry(50, 120, 120, 25)
		ells = ['«Не в работе»', '«В работе»', '«Сделка закрыта»', '«Отказ»']
		self.bCb.addItems(ells)

	def conted(self):
		self.conter = psycopg2.connect(
			database='postgress_intarface_db',
			user='postgres',
			password=password,
			host='127.0.0.1',
			port='')
		self.cur = self.conter.cursor()
	def get_logo_name(self):
		self.cur.execute('select login, FIO from user_table')
		self.itemsU = self.cur.fetchall()
		self.userfio = (i if self.user in i else None for i in self.itemsU)
		self.key = [*self.userfio]
		self.key = list(filter((None).__ne__, self.key))
		self.key = self.key[0][1]
class Usp(QWidget):
	def __init__(self, wg):
		self.wg = wg
		super().__init__(wg)
		self.userLayer = QVBoxLayout()

		self.uPt = QLabel(self.wg.key, self)


		self.btn = QPushButton('Закрыть')
		self.btn.clicked.connect(self.wg.close)
		self.btn.clicked.connect(self.wg.conter.close)

		self.userLayer.addWidget(self.uPt)
		self.userLayer.addStretch()
		self.userLayer.addWidget(self.btn)
		self.setLayout(self.userLayer)

class wIn(QTableWidget):
	def __init__(self, wg, key):
		self.wg = wg
		self.key = key
		super().__init__(wg)
		self.setGeometry(5, 5, 100, 200)
		self.setColumnCount(8)
		self.verticalHeader().hide()
		self.UppT()
	def UppT(self):
		self.clear()
		self.setRowCount(0)
		self.setHorizontalHeaderLabels(["Id_accounts",
										"Surname",
										"Name",
										"Middle_name",
										"Date_of_birth",
										"INN",
										"FIO_responsible",
										"STATUS"])
		self.wg.cur.execute('select * from client_table')
		itemsC = self.wg.cur.fetchall()
		i = 0
		for el in itemsC:
			self.setRowCount(self.rowCount() + 1)
			if self.key == el[-2]:
				j = 0
				for el1 in el:
					self.setItem(i, j, QTableWidgetItem(str(el1).strip()))
					j += 1
				i += 1
def startD():
	ppp = QApplication(sys.argv)
	exe = Face()
	exe.show()
	sys.exit(ppp.exec_())
def main():
	startD()
if __name__ == '__main__':
	main()