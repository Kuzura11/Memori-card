from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

app = QApplication([])
main_win = QWidget()

class Question():
    def __init__(self, question, right_answert,wron1,wron2,wron3):
        self.question = question
        self.right_answert = right_answert
        self.wron1 = wron1
        self.wron2 = wron2
        self.wron3 = wron3

def show_question():

    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')

    RadioGroup.setExclusive(False) 
    pon_1.setChecked(False)
    pon_2.setChecked(False)
    pon_3.setChecked(False)
    pon_4.setChecked(False)
    RadioGroup.setExclusive(True)
    
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def click_OK():
    
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answers) 
    answers[0].setText(q.right_answert) 
    answers[1].setText(q.wron1)
    answers[2].setText(q.wron2)
    answers[3].setText(q.wron3)
    qw.setText(q.question) 
    lb_Correct.setText(q.right_answert) 
    show_question()
    question_list.remove(q)

def check_answer():
    
    if answers[0].isChecked():
    
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%')

def show_correct(res):
    
    lb_Result.setText(res)
    show_result()
    
def next_question():
    
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    try:
        q = question_list[randint(0, len(question_list) - 1)] 
    except:
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
        exit()
    ask(q) 

question_list = []
question_list.append(Question('Кто призедент Росcии','В.В.Путин','Дмитрий Медведев','Джо Байден','И. В. Сталин'))
question_list.append(Question('В честь кого названа планета Нептун?','Римского бога','Открывшего её астронома','Греческого бога','Популярного в то время актёра'))
question_list.append(Question('Какой из этих овощей наиболее богат кальцием?','Брокколи','Капуста','Огурец','Морковь'))
question_list.append(Question('Сколько морей существует в мире?','73','334','55','83'))

RadioGroupBox = QGroupBox('Варианты ответа')
pon_1 = QRadioButton('Вариант 1')
pon_2 = QRadioButton('Вариант 2')
pon_3 = QRadioButton('Вариант 3')
pon_4 = QRadioButton('Вариант 4')

answers  = [pon_1,pon_2,pon_3,pon_4]

layot_ans1 = QVBoxLayout()
layot_ans2 = QHBoxLayout()
layot_ans3 = QHBoxLayout()

layot_ans2.addWidget(pon_1)
layot_ans2.addWidget(pon_2)
layot_ans3.addWidget(pon_3)
layot_ans3.addWidget(pon_4)
layot_ans1.addLayout(layot_ans2)
layot_ans1.addLayout(layot_ans3)
RadioGroupBox.setLayout(layot_ans1)

RadioGroup = QButtonGroup() 
RadioGroup.addButton(pon_1) 
RadioGroup.addButton(pon_2)
RadioGroup.addButton(pon_3)
RadioGroup.addButton(pon_4)


qw = QLabel("Вопрос")
button = QPushButton("Ответить")

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('?')
lb_Correct = QLabel('!')

da = QVBoxLayout()
da.addWidget(lb_Result)
da.addWidget(lb_Correct)
AnsGroupBox.setLayout(da)
AnsGroupBox.hide()


main_lay = QVBoxLayout()
main_lay.addWidget(qw)
main_lay.addWidget(RadioGroupBox)
main_lay.addWidget(AnsGroupBox)
main_lay.addWidget(button)

main_win.setLayout(main_lay)

button.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 1


main_win.show()
app.exec()




