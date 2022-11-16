import pyautogui as pg
import time
if __name__ == '__main__':
    tamano= pg.size ()
    print(tamano)
    boton_chrome=pg.locateOnScreen('.\s.png')
    siau=pg.locateOnScreen('.\siau.png')
    print(f'chrome = {boton_chrome}')
    pg.click(boton_chrome.left,boton_chrome.top)
    time.sleep(1)
    mas=pg.locateOnScreen('.\mas.png')
    pg.click(mas.left,mas.top)
    time.sleep(1)
    siau=pg.locateOnScreen('.\siau.png')
    pg.click(siau.left,siau.top)
    time.sleep(1)
    pg.write("deivid.hernandez") # usuario
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.write("alex8604ALEX;:_") # contraseña
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    with pg.hold('ctrl'):
        pg.press('t')

    pg.write("https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595")
    pg.press('enter')
    time.sleep(1)
    registrar=pg.locateOnScreen('.\sregistrar.png')
    pg.click(registrar.left, registrar.top)



    #historia=pg.locateOnScreen('.\historia.png')
    #pg.click(historia.left,historia.top)