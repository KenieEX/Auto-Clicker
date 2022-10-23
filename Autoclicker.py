import pyautogui
import keyboard

Kliker = int(input('Сколько кликов:'))
click = 1
key = 'b'
print('работа начата')
for click in range(0, Kliker):
    print('До конца осталось:' + str(+ Kliker))
    Kliker -= 1
    pyautogui.tripleClick()
    pyautogui.tripleClick()
    pyautogui.tripleClick()

    if keyboard.is_pressed(key):
        print('работа завершена')
        break
    else:
        continue
else:
    print('Конец')