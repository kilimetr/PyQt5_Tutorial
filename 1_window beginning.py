# window init with textlabel allign in box


from PyQt5 import QtWidgets
import sys

aplikace = QtWidgets.QApplication(sys.argv)
formular = QtWidgets.QWidget()
boxlayout = QtWidgets.QHBoxLayout()

popisek = QtWidgets.QLabel("Ahoj světe!!! Jsem naživu.",parent = formular)

formular.setGeometry(300,200,250,300)
formular.setWindowTitle("Moje první appka v PyQt5.")

boxlayout.addStretch()
boxlayout.addWidget(popisek)
boxlayout.addStretch()

formular.setLayout(boxlayout)
formular.show()
sys.exit(aplikace.exec())



