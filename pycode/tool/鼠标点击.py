import pyautogui
import time
def zuobiao():
    x, y = pyautogui.position()
    return(x,y)
def shishizuobiao():#shishishi shizuobiao  
    try:
      while True:
        x, y = pyautogui.position()
        print(x,y)
    except KeyboardInterrupt:
      print('\nExit.')
def click():
    pyautogui.click(button='left')
def click2(x1,y1):
    pyautogui.click(x=x1, y=y1, button='left')

def xunhuan():
    a1=0
    for x in range(0,150):
        print(a1)
        click2(zuobiao()[0],zuobiao()[1])
        time.sleep(4)
        a1+=1  
if __name__ == '__main__':
    xunhuan()
