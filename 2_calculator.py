# calculator

from PyQt5 import QtWidgets, QtGui
import sys

class Window(QtWidgets.QMainWindow):
	
	def __init__(self, **kwargs):
		super(Window, self).__init__(**kwargs)

		self.setWindowTitle("Calculator in PyQt5")
		self.init_gui()
		self.show()

	def init_gui(self):
		formular = QtWidgets.QWidget()
		formularLayout = QtWidgets.QVBoxLayout() # allign everything vertically
		formular.setLayout(formularLayout)

		boxLayout1 = QtWidgets.QHBoxLayout() # allign boxLayout1 horizontally
		boxLayout2 = QtWidgets.QHBoxLayout() # allign boxLayout2 horizontally

		formularLayout.addStretch()
		formularLayout.addLayout(boxLayout1)
		formularLayout.addLayout(boxLayout2)
		formularLayout.addStretch()

		self.vysledekLabel = QtWidgets.QLabel("0", self) # result 0 until calculating is initialized
		self.vysledekLabel.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))

		self.cislo1Edit = QtWidgets.QLineEdit(self)
		self.cislo2Edit = QtWidgets.QLineEdit(self)

		self.vypoctiButton = QtWidgets.QPushButton("Výpočet", self)

		self.operatorComboBox = QtWidgets.QComboBox(self)

		self.operatorComboBox.addItem("+")
		self.operatorComboBox.addItem("-")
		self.operatorComboBox.addItem("*")
		self.operatorComboBox.addItem("/")

		boxLayout1.addWidget(self.cislo1Edit)
		boxLayout1.addWidget(self.operatorComboBox)
		boxLayout1.addWidget(self.cislo2Edit)
		boxLayout1.addWidget(self.vysledekLabel)
		boxLayout2.addWidget(self.vypoctiButton)

		self.setCentralWidget(formular)

		self.vypoctiButton.clicked.connect(self.vypocti)

	def vypocti(self):
		vysledek = "";
		chyba = ""

		try:
			cislo1 = float(self.cislo1Edit.text())
			cislo2 = float(self.cislo2Edit.text())
			operator = self.operatorComboBox.currentText()

			if operator == "+":
				vysledek = cislo1 + cislo2
			elif operator == "-":
				vysledek = cislo1 - cislo2
			elif operator == "*":
				vysledek = cislo1 * cislo2
			elif operator == "/":
				if cislo2 == 0:
					chyba = "Deviding by 0"
				else:
					vysledek = cislo1 / cislo2

		except:
			chyba = "Number is unknown!"
			if chyba:
				self.vysledekLabel.setText(chyba)
			else:
				self.vysledekLabel.setText(str(round(vysledek,3)))

		self.vysledekLabel.setText(str(round(vysledek,3)))



aplikace = QtWidgets.QApplication(sys.argv)
okno = Window()
sys.exit(aplikace.exec_())

