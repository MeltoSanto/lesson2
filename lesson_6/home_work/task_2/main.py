from lesson_6.home_work.task_2.func import easy, medeum, hard

print('Привет!\n'
      'Ты открыл квиз "Аврора".\n'
      'Выбери сложность (1/2/3): ', end='')
level = input()

a = 1
while a == 1:
      if level == "1":
            easy()
            break
      elif level == "2":
            medeum()
            break
      elif level == "3":
            hard()
            break
      else:
            level = input("Выбери сложность корректно: ")