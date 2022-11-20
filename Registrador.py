import pyautogui as pg
import time
from Pc import Pc
from BuscaPaginaWeb import PaginaWeb

class Registrador:
    def __init__(self,imga):
        self.imga= imga
        
    def busca_boton(self,image):
        lista=[]
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
    verificador =objeto1.abre_apliacion(".\google_abierto.png")
    time.sleep(2)
    Sitio1=PaginaWeb("https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595")
    Sitio1.entra_pagina(verificador)
    time.sleep(2)

    registro1=Registrador([".\sboton1.png",".\s2_0_boton_registrar1.png",".\s2_0_boton_registrar2.png",".\s2_0_boton_registrar3.png",".\s2_0_boton_registrar4.png",".\s2_0_boton_registrar5.png"])
    for intento in registro1.imga:
        registro1.busca_con_comandos("registrar")
        time.sleep(1)
        lista_intentos=registro1.busca_boton(intento)
        print(f'{lista_intentos}')
        if lista_intentos!=None:
            x,y = lista_intentos
            break
    print(f'busca_boton {x} , {y}')
    pg.click(x,y,1)
