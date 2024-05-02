from PyQt5.QtWidgets import QApplication, QWidget
import sys

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = QWidget()
	w.resize(300, 300)
	w.setWindowTitle('TESTEROID')
	w.show()
	sys.exit(app.exec_())
