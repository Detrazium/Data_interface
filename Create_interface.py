from PyQt5.QtWidgets import (
	QApplication,
	QWidget,
	QPushButton,
	QTableWidgetItem,
	QMainWindow,
	QTableWidget,
	QLineEdit)
import sys
import psycopg2
from PyQt5 import QtGui


class Widjet(QWidget):
	def __init__(self):
		super().__init__()
		self.cont()

		self.setGeometry(100, 100, 700, 600)
		self.setWindowTitle('TEXT#1')
		self.tb = Tb(self)

		self.btn = QPushButton('Renove', self)
		self.btn.resize(150, 40)
		self.btn.move(500, 10)
		self.btn.clicked.connect(self.upd)

		self.idp = QLineEdit(self)
		self.idp.resize(150, 40)
		self.idp.move(500, 60)
		self.idp.setReadOnly(True)

		self.fio = QLineEdit(self)
		self.fio.resize(150, 40)
		self.fio.move(500, 110)

		self.oce = QLineEdit(self)
		self.oce.resize(150, 40)
		self.oce.move(500, 160)

		self.btn = QPushButton('Append', self)
		self.btn.resize(150, 40)
		self.btn.move(500, 210)
		self.btn.clicked.connect(self.ins)

		self.btn = QPushButton('Удалить', self)
		self.btn.resize(150, 40)
		self.btn.move(500, 260)
		self.btn.clicked.connect(self.dels)

	def cont(self):
		from GEN_table_information import password
		self.conn = psycopg2.connect(database='postgress_intarface_db',
									 user='postgres',
									 password=password,
									 host='127.0.0.1',
									 port='')
		self.cur = self.conn.cursor()

	def upd(self):
		self.conn.commit()
		self.tb.updt()
		self.idp.setText('')
		self.fio.setText('')
		self.oce.setText('')

	def ins(self):
		fio, oce = self.fio.text(), self.oce.text()
		try:
			self.cur.execute('ist')
		except:
			pass
		self.upd()

	def dels(self):
		try:
			ids = int(self.idp.text())
		except:
			return
		self.cur.execute('delExempter')
		self.upd()


class Tb(QTableWidget):
	def __init__(self, wg):
		self.wg = wg
		super().__init__(wg)
		self.setGeometry(10, 10, 400, 500)
		self.setColumnCount(10)
		self.verticalHeader().hide();
		self.updt()
		self.setEditTriggers(QTableWidget.NoEditTriggers)
		self.cellClicked.connect(self.cellClick)

	def updt(self):
		self.clear()
		self.setRowCount(0);
		self.setHorizontalHeaderLabels(['id', 'fio', 'price', 'date#1', 'date@2'])
		self.wg.cur.execute('select * from user_table')
		rows = self.wg.cur.fetchall()
		i = 0
		for elem in rows:
			self.setRowCount(self.rowCount() + 1)
			j = 0
			for t in elem:
				self.setItem(i, j, QTableWidgetItem(str(t).strip()))
				j += 1
			i += 1
		self.resizeColumnsToContents()

	def cellClick(self, row, col):
		self.wg.idp.setText(self.item(row, 0).text())
		self.wg.fio.setText(self.item(row, 1).text().strip())
		self.wg.oce.setText(self.item(row, 0).text().strip())


app = QApplication(sys.argv)
ex = Widjet()
ex.show()
sys.exit(app.exec_())
