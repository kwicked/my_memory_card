#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,  QHBoxLayout, QVBoxLayout,QRadioButton, QMessageBox, QGroupBox, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

quest_list = []
quest_list.append(Question('Государственный язык Бразилии','Португальский','Бразильский','Испанский','Итальянский'))
quest_list.append(Question('Сколько букв всловеёж?','8','27','Олег','2'))
quest_list.append(Question('Как зовут Егора Крида?','Анфиса','Егор','Олег','Крид'))
quest_list.append(Question('Сколько будет 1 + 1?','Англия','2','42','10'))
quest_list.append(Question('Татьяна в каком году 45 дней?','Чтаа','Дмитрий','Олег','2'))
quest_list.append(Question('Как звали Менделеева?','Дмитрий','Иван','Афанасий','Прокофий'))
quest_list.append(Question('Что потеряла золушка, когда бежала от принца?','Туфельку','Трусы','Платок','Кольцо'))
quest_list.append(Question('Сколько букв в слове а?','10','1','а','2'))
quest_list.append(Question('Чего мало в клипе Ольги Бузовой?','Мозгов','Половин','Воды','Ольги Бузовой'))
quest_list.append(Question('Глаза боятся, а руки..?','делают','умеют','собирают','убирают'))

app = QApplication([])
quest = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
groubox = QGroupBox('Варианты ответов')

rb1 = QRadioButton('Энцы')
rb2 = QRadioButton('Смурфы')
rb3 = QRadioButton('Чулымцы')
rb4 = QRadioButton('Алеуты')

laut_ans1 = QHBoxLayout()
laut_ans2 = QVBoxLayout()
laut_ans3 = QVBoxLayout()
laut_ans2.addWidget(rb1)
laut_ans2.addWidget(rb2)
laut_ans3.addWidget(rb3)
laut_ans3.addWidget(rb4)
laut_ans1.addLayout(laut_ans2)
laut_ans1.addLayout(laut_ans3)
groubox.setLayout(laut_ans1)
'''groubox.hide()'''
lautq1 = QHBoxLayout()
lautq2 = QHBoxLayout()#варианты ответов или результат теста
lautq3 = QHBoxLayout()#кнопка ответить
lautq1.addWidget(quest, alignment=(Qt.AlignCenter| Qt.AlignCenter))
lautq2.addWidget(groubox)
lautq2.addStretch(1)
lautq3.addWidget(button, stretch = 2)
lautq3.addStretch(1)
laytcar = QVBoxLayout()
laytcar.addLayout(lautq1, stretch=2)
laytcar.addLayout(lautq2, stretch=8)
laytcar.addStretch(1)
laytcar.addLayout(lautq3, stretch=1)
laytcar.addStretch(1)
laytcar.addSpacing(5)
AnsGroupBox = QGroupBox("Результат теста")
riglos = QLabel('Верно/Невернно')
righ = QLabel('Правильный ответ/Неправильный ответ')
laut_3 = QVBoxLayout()
laut_3.addWidget(riglos)
laut_3.addWidget(righ)
AnsGroupBox.setLayout(laut_3)
def show_result():
    groubox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
def show_question():
    groubox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    RadioGroup.setExclusive(True)
'''def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()'''

answers = [rb1, rb2, rb3, rb4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quest.setText(q.question)
    righ.setText(q.right_answer)
    show_question()
def show_correct(res):
    riglos.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Верно!')
        main.score += 1
        print('Статистика\n-Всего вопросов: ', main.total, '\n-Правильных ответов:', main.score)
        print('Рейтинг: ', (main.score/main.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно!')
def next_question():
    main.total += 1
    print('Статистика\n-Всего вопросов: ', main.total, '\n-Правильных ответов:', main.score)
    cur_quest = randint(0, len(quest_list) - 1)
    '''main.cur_quest = main.cur_quest + 1
    if main.cur_quest >= len(quest_list):
        main.cur_quest = 0'''
    q = quest_list[cur_quest]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main = QWidget()
main.setLayout(laytcar)
main.setWindowTitle('Claboe zveno')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rb1)
RadioGroup.addButton(rb2)
RadioGroup.addButton(rb3)
RadioGroup.addButton(rb4)
#ask('Государственный язык Бразилии','Португальский','Бразильский','Испанский','Итальянский')



button.clicked.connect(click_OK) 
main.score = 0
main.total = 0
next_question()
main.show()
app.exec_()