from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 


class Question():
     #  bir soru, bir doğru cevap ve üç yanlış cevap içerir
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = [] 
questions_list.append(
        Question('Brezilya\'nın resmi dili', 'Portekizce', 'İngilizce', 'İspanyolca', 'Brezilyaca'))
questions_list.append(
        Question('Rusya bayrağında hangi renk yoktur?', 'Yeşil', 'Kırmızı', 'Beyaz', 'Mavi'))
questions_list.append(
        Question('Yakutların yöresel evleri', 'Urasa', 'Yurt', 'İglo', 'Peri bacaları'))


app = QApplication([])


btn_OK = QPushButton('Cevapla') # cevap düğmesi
lb_Question = QLabel('Dünyadaki en zor soru!') # soru metni


RadioGroupBox = QGroupBox("Cevap seçenekleri") # cevapları olan anahtarlar için ekranda bir grup


rbtn_1 = QRadioButton('Seçenek 1')
rbtn_2 = QRadioButton('Seçenek 2')
rbtn_3 = QRadioButton('Seçenek 3')
rbtn_4 = QRadioButton('Seçenek 4')


RadioGroup = QButtonGroup() # bu, anahtar davranışlarının kontrol edilebilmesi için anahtarları gruplandırmak içindir
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # dikey olanlar yatay olanın içinde olacak
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # ilk sütuna iki cevap
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # ikinci sütuna iki cevap
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # sütunlar tek satıra yerleştirildi


RadioGroupBox.setLayout(layout_ans1) # cevap seçeneklerini içeren "panel" hazır 


AnsGroupBox = QGroupBox("Test sonucu")
lb_Result = QLabel('doğru mu yanlış mı?') # buraya "doğru" veya "yanlış" yazısı yerleştirilir"
lb_Correct = QLabel('cevap burda olacak!') # doğru cevabın metni burada yazılmış olacaktır


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # soru
layout_line2 = QHBoxLayout() # cevap seçenekleri veya test sonucu
layout_line3 = QHBoxLayout() # "Cevapla" düğmesi


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # cevap panelini gizleyelim, önce soru paneli gözükmelidir


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # düğme büyük olmalı
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # içerik arasındaki boşluklar
def show_result():
     #  cevap panelini gösteriniz 
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Sıradaki soru')


def show_question():
   #  soru panelini gösteriniz 
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Cevapla')
    RadioGroup.setExclusive(False) # radyo düğme seçiminin sıfırlanabilmesi için kısıtlamalar kaldırıldı
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # kısıtlamalar geri getirildi, şimdi sadece bir radyo düğmesi seçilebilir


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
     #  fonksiyon, soru ve cevapların değerlerini ilgili widgetlara yazar, cevap seçenekleri ise rastgele dağıtılır 
    shuffle(answers) # düğme listesi karıştırıldı, artık listenin ilk sırasında öngörülemeyen bir düğme var
    answers[0].setText(q.right_answer) # listenin ilk öğesini doğru cevapla dolduralım, geriye kalanlar yanlış cevaplarla doldurulacak
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # soru
    lb_Correct.setText(q.right_answer) # cevap 
    show_question() # soru panelini gösteriyoruz 


def show_correct(res):
    #  sonucun gösterilmesi - iletilen metni "sonuç" etiketine yerleştirelim ve gerekli paneli gösterelim 
    lb_Result.setText(res)
    show_result()


def check_answer():
    #  eğer herhangi bir cevap seçeneği seçili ise kontrol edilip cevap panelinin gösterilmesi gerekmektedir
    if answers[0].isChecked():
        # doğru cevap!
        show_correct('Doğru!')
        window.score += 1
        print('İstatistik\n-Toplam soru: ', window.total, '\n-Doğru cevap: ', window.score)
        print('Puanlama: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # yanlış cevap!
            show_correct('Yanlış!')
            print('Puanlama: ', (window.score/window.total*100), '%')
    


def next_question():
    # listeden rastgele bir soru sorar 
    window.total += 1
    print('İstatistik\n-Toplam soru: ', window.total, '\n-Doğru cevap: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # eski değere ihtiyaçımız yoktur, 
                                                        # bu nedenle lokal bir değişken kullanılabilir! 
            # rastgele listeden bir soru alındı
            # yaklaşık yüz kelime girilirse, nadiren tekrarlanır
    q = questions_list[cur_question] # soruyu aldık
    ask(q) # soruldu


def click_OK():
    ''' başka sorunun gösterilip gösterilmeyeceğini veya bu soruya verilen cevabın kontrol edilip edilmeyeceğini belirler'''
    if btn_OK.text() == 'Cevapla':
        check_answer() # cevabın kontrolü
    else:
        next_question() # sıradaki soru


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')


btn_OK.clicked.connect(click_OK) # butona tıklayarak tam olarak ne olacağını seçiyoruz


window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
