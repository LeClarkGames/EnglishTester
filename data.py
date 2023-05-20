from random import shuffle
from app_layout import *
from pygame import mixer
import os

sound_mixer = mixer
sound_mixer.init()

class Questions:
    def __init__(self, right, wrong1, wrong2, wrong3, wrong4, wrong5, sound):
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.wrong4 = wrong4
        self.wrong5 = wrong5
        self.sound = sound

    def make_sound(self):
        sound_mixer.music.load(self.sound)
        sound_mixer.music.play()

    def stop_sound(self):
        sound_mixer.music.stop(self.sound)

    def show_data(self, result_answ, btn_list):
        result_answ.setText(self.right)
        shuffle(btn_list)
        btn_list[0].setText(self.right)
        btn_list[1].setText(self.wrong1)
        btn_list[2].setText(self.wrong2)
        btn_list[3].setText(self.wrong3)
        btn_list[4].setText(self.wrong4)
        btn_list[5].setText(self.wrong5)

    def check_result(self, btn_list, result):
        if btn_list[0].isChecked():
            result.setText("Right!")
            result.setStyleSheet("background: rgb();")
        else:
            result.setText("Wrong!")
            result.setStyleSheet("background: rgb();")

q1 = Questions("A jug fills drop by drop", "A jug fils drop buy drap", "A jag fillc drap by drop", "E jag fulls drop by grap", "Jug fills by drap", "A jug fels drag by drap", "E:/Python/English Tester [My Project]/Additional Files/Sounds/A jug fills drop by drop.mp3")
q2 = Questions("Don't ruin the present with the ruined past", "Dont run the precent wif ze ruind pasg", "Don't rain the prezent with the rained paet", "Don'd rin they present wij the ruined pest", "Dont ruin present the ruined past", "Don't pain thes prest wit the rauined rast", "E:/Python/English Tester [My Project]/Additional Files/Sounds/Don't ruin the present with the ruined past.mp3")
q3 = Questions("Freedom is the right to live as we wish", "Fredom iz the rigt liv os we wis", "Freedom ze righ do live as wish", "Reetom is riht live us ve fish", "Freedom s right to leave fe wich", "Reedom iz zhe righ to wish", "E:/Python/English Tester [My Project]/Additional Files/Sounds/Freedom is the right to live as we wish.mp3")
q4 = Questions("He that is giddy thinks the world turns round", "She hat is gidy hiks the wold urns raund", "Hes het z kiddy thinks world turn around", "He is gidu thikzze wold tarn ound", "Thad is giddy thinks world rand", "Hi is kitty thiss th wod taurns ren", "E:/Python/English Tester [My Project]/Additional Files/Sounds/He that is giddy thinks the world turns round.mp3")
q5 = Questions("I want more detailed information", "Ai went mere detaled formation", "I wont more detiled informatien", "I vont detailet information", "Oi wot mor detailed infarmation", "Want mof detailid information", "E:/Python/English Tester [My Project]/Additional Files/Sounds/I want more detailed information.mp3")
q6 = Questions("If you wish to be a writer - write", "If ouy wish be a wrider - wdite", "Fi you wik do be writer - write", "If wish de e writer - write", "Iw you to be a wrirer - wrire", "If yoi to be wrider - wrid", "E:/Python/English Tester [My Project]/Additional Files/Sounds/If you wish to be a writer, write.mp3")
q7 = Questions("In the middle of every difficulty lies opportunity", "In midle of ever dificult lis opportunity", "In the midle ewery difficulty lies oportunity", "In ze medle every difficulty lies opportunity", "In the midlie of every dificulty lies oportuniy", "In the midle ow very difficultu lies pportunity", "E:/Python/English Tester [My Project]/Additional Files/Sounds/In the middle of every difficulty lies opportunity.mp3")
q8 = Questions("She saw the brake lights, but not in time", "He saf the brake lights, bud no time", "She the brake light, not in dime", "She saw brade lights, but in time", "She saf the rake ligts, but nod in", "She sow tho rokee lits, not in time", "E:/Python/English Tester [My Project]/Additional Files/Sounds/She saw the brake lights, but not in time.mp3")
q9 = Questions("Silence is a source of great strength", "Silense a source of gret stength", "Sielinence is sure of great stngth", "Soilnese is source of great renth", "Silnce a sococe af gret stgth", "Soilense is you course graet strength", "E:/Python/English Tester [My Project]/Additional Files/Sounds/Silence is a source of great strength.mp3")
q10 = Questions("Study the past, if you would divine the future", "Study ze past, if wold divine the future", "Studie the past, foif would divine the fyture", "Stody past, you would devie the future", "Stoiduy the post, if wauld divine fyture", "Stoudy the past, you woud dive ze future", "E:/Python/English Tester [My Project]/Additional Files/Sounds/Study the past, if you would divine the future.mp3")

quest_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]