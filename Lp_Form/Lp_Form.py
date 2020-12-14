import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QLineEdit,QTextEdit, QComboBox, QMainWindow, QPushButton, QApplication,QLabel, QMessageBox)
from PyQt5.QtGui import QFont 
from scipy.optimize import linprog
import designer

class Form(QWidget):
    def __init__(self):
        super().__init__()
        designer.init(self)


    def paramsReset(self):
        self.radioAutitory = self.RadioAudience.text()
        self.televisionAuditory = self.TVAudience.text()
        self.totalAuditory = self.GeneralAudience.text()
        self.radioUpperLimit = self.Radio.text() 
        self.totalBedget = self.Budget.text()
        self.radioMinuteCost = self.CostRadio.text()
        self.televisionMinuteCost = self.TVCost.text()
        self.radioAgents = self.AgentsRadio.text()
        self.televisionAgents =  self.TVAgents.text()
        self.totalAgentsCount = self.Count.text()

    def task1(self):
        self.paramsReset()
        res = self.solve([0, 0, 2, 0, 0, 1],[],[])
        self.Result.setText(str(res))

 
    def task2(self):
        self.paramsReset()
        buf = self.solve([0, 0, 1, 0, 0, 0], [], [])
        s1 = buf.x[2]
        res = self.solve([0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0], s1)
        self.Result.setText(str(res))

    def solve(self, c, A, b):
        A_eq = [[int(self.radioAutitory), int(self.televisionAuditory), 1, -1, 0, 0],[int(self.radioMinuteCost), int(self.televisionMinuteCost), 0, 0, 1, -1]]
        b_eq = [int(self.totalAuditory), int(self.totalBedget)]
        A_ub = [[int(self.radioAgents), int(self.televisionAgents), 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
        b_ub = [int(self.totalAgentsCount), int(self.radioUpperLimit)]
        bounds = [(0, None), (0, None), (0, None), (0, None), (0, None), (0, None)]
        if len(A) != 0:
            A_eq.append(A)
            b_eq.append(b)
        res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)
        return res

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())  

