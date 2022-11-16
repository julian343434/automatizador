import pyautogui as pg
import time
from Pc import Pc
from BuscaPaginaWeb import PaginaWeb

class Registrador:
    def __init__(self,imga):
        self.imga= imga
        
    def busca_boton(self,image):
        Cord_boton=pg.locateCenterOnScreen(image)
        print(Cord_boton)
        return Cord_boton
    
    @classmethod
    def busca_con_comandos(cls,palabra):
        with pg.hold("ctrl") :
            pg.press("f")
        pg.write(palabra)

if __name__ == "__main__":
    objeto1= Pc("chrome")
    verificador =objeto1.abre_apliacion()
    time.sleep(2)
    Sitio1=PaginaWeb("https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595")
    Sitio1.entra_pagina(verificador)
    time.sleep(2)

    registro1=Registrador(".\sboton1.png")
    print(f'{registro1.imga}')
    x, y=registro1.busca_boton()
    print(f'busca_boton {x} , {y}')
   ## pg.click(x,None)"
