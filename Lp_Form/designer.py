from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont 

def init(Form):

    Form.radioAutitory = 0
    Form.televisionAuditory = 0
    Form.totalAuditory = 0
    Form.radioUpperLimit = 0
    Form.totalBedget = 0
    Form.radioMinuteCost = 0
    Form.televisionMinuteCost = 0
    Form.radioAgents = 0
    Form.televisionAgents = 0
    Form.totalAgentsCount = 0

    lbl1 = QLabel('Радио', Form)
    lbl1.move(240, 10)
    lbl2 = QLabel('Телевидение', Form)
    lbl2.move(375, 10)
    lbl3 = QLabel('Рекламная аудитория(млн.чел.)', Form)
    lbl3.move(10, 45)
    lbl4 = QLabel('Стоимость(тыс. $.)', Form)
    lbl4.move(10, 75)
    lbl5 = QLabel('Количество рекламных агентов, шт.', Form)
    lbl5.move(10, 105)
    lbl6 = QLabel('Бюджет, тыс. $', Form)
    lbl6.move(10, 245)
    lbl7 = QLabel('Общее количество агентов, шт', Form)
    lbl7.move(10, 155)
    lbl8 = QLabel('Аудитория не менее, тыс. шт.', Form)
    lbl8.move(10, 185)
    lbl9 = QLabel('Реклама на радио не более, минут', Form)
    lbl9.move(10, 215)


    Form.RadioAudience = QLineEdit(Form)
    Form.RadioAudience.move(210, 40)
    Form.RadioAudience.resize(100, 20)

    Form.TVAudience = QLineEdit(Form)
    Form.TVAudience.move(360, 40)
    Form.TVAudience.resize(100, 20)

    Form.Count = QLineEdit(Form)
    Form.Count.move(210, 150)
    Form.Count.resize(100, 20)

    Form.GeneralAudience = QLineEdit(Form)
    Form.GeneralAudience.move(210, 180)
    Form.GeneralAudience.resize(100, 20)

    Form.CostRadio = QLineEdit(Form)
    Form.CostRadio.move(210, 70)
    Form.CostRadio.resize(100, 20)

    Form.TVCost = QLineEdit(Form)
    Form.TVCost.move(360, 70)
    Form.TVCost.resize(100, 20)

    Form.Radio = QLineEdit(Form)
    Form.Radio.move(210, 210)
    Form.Radio.resize(100, 20)

    Form.Budget = QLineEdit(Form)
    Form.Budget.move(210, 240)
    Form.Budget.resize(100, 20)

    Form.AgentsRadio = QLineEdit(Form)
    Form.AgentsRadio.move(210, 105)
    Form.AgentsRadio.resize(100, 20)

    Form.TVAgents = QLineEdit(Form)
    Form.TVAgents.move(360, 100)
    Form.TVAgents.resize(100, 20)

    Form.Result = QTextEdit(Form)
    Form.Result.move(10, 300)
    Form.Result.resize(460, 200)

    btn1 = QPushButton('Метод\nвесовых\nкоэффициентов', Form)
    btn1.resize(100, 50)
    btn1.move(360, 150)  
    btn1.clicked.connect(Form.task1)

    btn2 = QPushButton('Метод\nприоритетов', Form)
    btn2.resize(100, 50)
    btn2.move(360, 210)  
    btn2.clicked.connect(Form.task2)

    Form.show()
