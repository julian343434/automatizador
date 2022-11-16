from BuscaPaginaWeb import PaginaWeb
import pyautogui as pg
import time 
from Pc import Pc
from Registrador import Registrador

class Usuario(Registrador):
    def __init__(self,NombreUsuario,Contrasena) -> None:
        self._NombreUsuario= NombreUsuario
        self._Contrasena= Contrasena

    @property
    def NombreUsuario(self):
        return self._NombreUsuario
    
    @NombreUsuario.setter
    def NombreUsuario(self,NombreUsuario):
        self._NombreUsuario = NombreUsuario 

    def empaqueta(self):
        lista =[]
        lista.append(self._NombreUsuario)
        lista.append(self._Contrasena)
        return lista
    

    def test_pagina(self):
        Registrador.busca_con_comandos("rol")
        dentro_siau=Registrador.busca_boton(".\stest_siau_pag_principal.png")
        if afuera_siau_x ==None and afuera_siau_y == None:
            if dentro_siau==None:
                return False , False , False
            else:
                return True , True , True
        else:
            with pg.hold("ctrl"):
                pg.press("r")
            return True , True ,False


    def EntraCredenciales(self):
        credenciales=Usuario.empaqueta(self)
        for credenciales in credenciales:
            pg.write(credenciales)
            pg.press("tab")
        pg.press("enter")
        print("se ingresaron las credenciales ")
        time.sleep(3)
        return True


if __name__ == "__main__":
    cont=0    
    objeto1 =Pc("chrome")
    Sitio1=PaginaWeb("https://siau.unillanos.edu.co:8443/ORION/Login")   
    s=input("ingresa tu usuario de siau")
    m=input("ingresa tu contraseña")
    link=input("ingresa tu link de comedor siau ")
    usiario1=Usuario(s,m)

    Sitio2= PaginaWeb(link)


    abierto_chrome1=False
    abierto_pagina1=False
    credenciales_entradas=False

    while True:
        if abierto_chrome1 == False:
            abierto_chrome1=objeto1.abre_apliacion()
        else:
            if abierto_pagina1 == False:
                abierto_pagina1=Sitio1.entra_pagina(abierto_chrome1)
            else:
                if credenciales_entradas==False:
                    credenciales_entradas=usiario1.EntraCredenciales()
                    Registrador.busca_con_comandos("consultar")
                    registro2=Registrador(".\stest_siau_inicio.png")
                    try:
                        x,y = registro2.busca_boton(registro2.imga)
                    except TypeError:
                        with pg.hold("ctrl"):
                            pg.press("r")
                        Registrador.busca_con_comandos("rol")
                        try:
                            registro3=Registrador(".\stest_siau_pag_principal.png")
                        except TypeError:
                            print("hubo un error")
                            abierto_chrome1, abierto_pagina1,credenciales_entradas= False,False,False
                        ##abierto_chrome1 , abierto_pagina1 ,credenciales_entradas =usiario1.test_credenciales()
                    Sitio1.cerrar_pagina()            
                else:
                    chrome2=objeto1.abre_apliacion()
                    abierto_pagina2=Sitio2.entra_pagina(abierto_chrome1)
                    try:
                        Registrador.busca_con_comandos("registrar")
                        registro1=Registrador(".\sboton1.png")
                        x, y =registro1.busca_boton(registro1.imga)
                        pg.moveTo(x,y,2)
                        pg.click(x,y)
                        time.sleep(10)
                        Sitio2.cerrar_pagina()
                        break 
                    except TypeError:
                        print("no se registro el almuerzo")






                



    