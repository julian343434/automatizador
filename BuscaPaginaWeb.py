import pyautogui as pg
import time 
from Pc import Pc

class PaginaWeb:
    def __init__(self,SitioWeb) -> None:
        self.SitioWeb = SitioWeb

    @classmethod
    def recargar_pagina(cls):
        with pg.hold("ctrl"):
            pg.press("r")

    @classmethod
    def cerrar_pagina(cls):
        with pg.hold("ctrl"):
            pg.press("w")

    def entra_pagina(self,pagina_abierta):
        if pagina_abierta == True :
            pg.write(self.SitioWeb)
            pg.press("enter")
            print(f'se ha ingresado en el sitio web {self.SitioWeb}')          
            print("¡¡Proceso Exitoso¡¡")
        else:
            Pc.abre_apliacion()
        time.sleep(3)
    

if __name__ == "__main__":
    objeto1= Pc("chrome")
    verificador =objeto1.abre_apliacion(".\googl_inicio.png")
    time.sleep(2)
    Sitio1=PaginaWeb("https://siau.unillanos.edu.co:8443/ORION/Login")
    Sitio1.entra_pagina(verificador)
    time.sleep(2)
    PaginaWeb.recargar_pagina()
