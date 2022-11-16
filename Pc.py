import pyautogui as pg
import time

class Pc:
    def __init__(self,aplicacion):
        self.aplicacion =aplicacion

    def abre_apliacion(self):
        pg.press('win')
        time.sleep(1)
        pg.write(self.aplicacion)
        pg.press("enter")
        time.sleep(5)
        pagina_verdadera = pg.locateCenterOnScreen(".\pagina_VERDADERA.png")
        print(f'pagina_verdadera = {pagina_verdadera}')
        time.sleep(5)      
        
        
        if pagina_verdadera == None:
            with pg.hold("ctrl"):
                pg.press("t")
            time.sleep(1)
            with pg.hold("ctrl"):           
                with pg.hold("shift"):
                    pg.press("tab")
            time.sleep(2)
            with pg.hold("ctrl"):
                pg.press("w")
            time.sleep(2)
            print(f'se ha ingresado a {self.aplicacion} con forzamiento')
            return True
        else  :
            print(f'se ha ingresado a {self.aplicacion} sin forzar')    
            print("¡¡Proceso exitoso¡¡")
            time.sleep(5)
            return True


if __name__ == '__main__':
    objeto1= Pc("chrome")
    objeto1.abre_apliacion()
