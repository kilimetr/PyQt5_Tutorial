

from PyQt5 import QtWidgets, uic
import os

os.chdir("/Users/kilimetr/Desktop/python/pyqt")


def main():
	app = QtWidgets.QApplication([])

	window = QtWidgets.QMainWindow()

	with open("mainwindow.ui") as f:
		uic.loadUi(f, window)

	window.show()

	return app.exec()

main()
