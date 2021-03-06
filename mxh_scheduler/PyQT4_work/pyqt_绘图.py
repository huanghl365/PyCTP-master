#!/usr/bin/python

# drawtext.py

import sys
from PyQt4 import QtGui, QtCore


class DrawText(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Draw Text')

        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'



    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setPen(QtGui.QColor(168, 34, 3))
        paint.setFont(QtGui.QFont('Decorative', 10))
        paint.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)
        paint.end()


app = QtGui.QApplication(sys.argv)
dt = DrawText()
dt.show()
app.exec_()