import pyautogui
import time

pyautogui.alert('O código esta iniciando, não toque no teclado nem no mouse.')
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)

pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd') #com o hotkey, nós utilizamos da combinação de taclas ou utilizamos as teclas de atalho.
pyautogui.moveTo(32, 530)
pyautogui.mouseDown()
pyautogui.moveTo(927, 833)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.mouseUp()

time.sleep(5)

pyautogui.alert('O código esta finalizado, pode utilizar normalmente.')