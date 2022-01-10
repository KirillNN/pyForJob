# https://www.youtube.com/watch?v=iZzx1keKztY
# https://pyautogui.readthedocs.io/en/latest/
import pyautogui
from time import sleep

# пауза и досрочное прекращение
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
repeat = 16

# разрешение экрана и позиция
print(pyautogui.size())
# for _ in range(100):
#     print(pyautogui.position())
#     sleep(1)

# Перемещение мыши
# pyautogui.moveTo(3840 / 2, 2160 / 2, duration=1)
# pyautogui.move(-200, -200, duration=2)

# нажатие
# pyautogui.click()
# pyautogui.doubleClick()
# pyautogui.tripleClick()
# pyautogui.rightClick()
# sleep(2)
# pyautogui.keyDown('enter')

# ввод с клавиатуры
# pyautogui.typewrite('Hello, World!', interval=0.2)

# нажатие клавиш: press, hotkey
# sleep(0.5)
# pyautogui.press('enter')

for _ in range(repeat):
    pyautogui.moveTo(2628, 275, duration=0.1)
    pyautogui.click()
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.moveTo(3022, 275, duration=0.1)
    pyautogui.click()
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.moveTo(3219, 348, duration=0.1)
    pyautogui.click()
