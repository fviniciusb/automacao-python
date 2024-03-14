import pyautogui as pa
import time
# import keyboard
pa.PAUSE = 1


question = input('deseja continuar? \n')


while question == 'sim':
    time.sleep(2)
    pa.click(x=947, y=1040)
    pa.write('alguma coisa aleatoria pq isso aq é um teste')
    pa.press('enter')    
    pa.press('win')
    pa.write('whatsapp')
    pa.press('enter')
else:
    print('ta ok')