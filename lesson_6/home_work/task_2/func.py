import json
import random
from random import randint


def inp_symb(a): # тире для красивого списка команд
    aa = []
    for i in range(a):
        aa.append('-')
    return ''.join(aa)


def get_options(ans):
    with open("files/answers.json", "r") as answers:
        read = answers.read()
        transl = json.loads(read)
        prom = transl[str(ans)]
        prom1 = prom.split()

        pre_ans_list = []
        pre_ans_list.append(str(abs(int(prom1[0]) - randint(15, 20))))
        pre_ans_list.append(str(int(prom1[0]) + randint(1, 5)))
        pre_ans_list.append(prom1[0])
        random.shuffle(pre_ans_list)

        return " / ".join(pre_ans_list)


def process(count):
    with open("files/questions.json", "r") as questions, open("files/answers.json", "r") as  answers:
        read_q = questions.read()
        read_a = answers.read()
        transl_q = json.loads(read_q)
        transl_a = json.loads(read_a)

        control = []
        score = 0

        a = 1
        while a <= count:
            ran = randint(1, 10)
            if ran in control:
                continue
            else:
                control.append(ran)
                a += 1
            print(f'Вопрос №{a-1}: {transl_q[str(ran)]} - Варианты ответа: {get_options(ran)}.')

            prom = transl_a[str(ran)]
            prom1 = prom.split()

            answer = input("Введите ответ одним числом: ")
            g = 1
            while g == 1:
                if answer.isdigit() == True:
                    if answer == prom1[0]:
                        score += 1
                        print(f"Правильно! Счёт: {score}\n")
                        break
                    else:
                        print(f"Ответ не верный. Правильный ответ - {prom}.\n")
                        break
                else:
                    answer = input("Не могу понять, введите ответ числом: ")

        if score >= 2:
            print(f"Ура! Ты победил! Твой счёт: {score}.\nПопробуй ещё!")
        elif score < 2:
            print(f"Нееет! Ты проиграл! Твой счёт: {score}.\nПопробуй ещё!")


def easy():
    print(f"\n{inp_symb(100)}\n"
          f"Выбрана ПРОСТАЯ сложность. Для победы, дайте правильный ответ хотя бы на 2 вопроса из 3х.\n"
          f"{inp_symb(100)}\n")
    process(3)

def medeum():
    print(f"\n{inp_symb(100)}\n"
          f"Выбрана СРЕДНЯЯ сложность. Для победы, дайте правильный ответ хотя бы на 4 вопроса из 6ти.\n"
          f"{inp_symb(100)}\n")
    process(6)


def hard():
    print(f"\n{inp_symb(100)}\n"
          f"Выбрана ВЫСОКАЯ сложность. Для победы, дайте правильный ответ хотя бы на 7 вопросов из 10ти.\n"
          f"{inp_symb(100)}\n")
    process(10)