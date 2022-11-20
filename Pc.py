import pyautogui as pg
import time
import webbrowser
class Pc:
    def __init__(self,aplicacion):
        self.aplicacion =aplicacion

    @classmethod
    def apagar_Pc(cls):
        time.sleep(5)
        with pg.hold("win"):
            pg.press("x")
        pg.press("up")
        pg.press("up")
        pg.press("right") 
        pg.press("down")
        pg.press("down")
        time.sleep(2)
        pg.press("enter")

    def abre_apliacion(self,image):
        pg.press('win')
        time.sleep(1)
        pg.write(self.aplicacion)
        pg.press("enter")
        time.sleep(5)
        palabra="buscar en google"
        try:
            Cord_boton=pg.locateCenterOnScreen(image)
            print(Cord_boton)
        except Exception :
            pagina_verdadera= None
        with pg.hold("ctrl") :
            pg.press("f")
        pg.write(palabra)        
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

    webbrowser.open_new_tab("https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595")
    ##objeto1= Pc("chrome")
    ##objeto1.abre_apliacion(".\google_inicio.png")
