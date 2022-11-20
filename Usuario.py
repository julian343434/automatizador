from BuscaPaginaWeb import PaginaWeb
import pyautogui as pg
import time 
from Pc import Pc
from Registrador import Registrador
import webbrowser as chrome
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
        pass
     ##   Registrador.busca_con_comandos("rol")
      ##  dentro_siau=Registrador.busca_boton(".\stest_siau_pag_principal.png")
        ##if afuera_siau_x ==None and afuera_siau_y == None:
        ##    if dentro_siau==None:
         ##       return False , False , False
         ##   else:
         ##       return True , True , True
      ##  else:
       ##     with pg.hold("ctrl"):
        ##        pg.press("r")
        ##    return True , True ,False

    def EntraCredenciales(self):
        credenciales=Usuario.empaqueta(self)
        for credenciales in credenciales:
            pg.write(credenciales)
            time.sleep(1)
            pg.press("tab")
        pg.press("enter")
        print("se ingresaron las credenciales ")
        time.sleep(3)
        return True

if __name__ == "__main__":
    ## Espera unos minutos
    time.sleep(5)
    ## Termina la espera
    
    ##instancias
    objeto1= Pc("chrome")
    objeto1.abre_apliacion(".\google_inicio.png")
    ##
    time.sleep(15)

    ## abre la pagina del almuerzo
    chrome.open_new_tab("https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595")
    chrome.open_new_tab("https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062585")
    ##links= ["https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062585","https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595"]

    ##variables
    cont=0
    ## 

    time.sleep(5)
    ## autenticador de sitio
    while cont<2:
        while True:
            try:
                time.sleep(1)
                registro2=Registrador([".\sboton1.png",".\s2_0_registro_exitoso_1.png",".\s2_0_registro_exitoso_2.png","s2_0_registro_exitoso_3","s2_0_registro_exitoso_4","s2_0_registro_exito_5.png","s2_0_registro_exitoso_6.png"])
                for intento in registro2.imga:
                        Registrador.busca_con_comandos("no quedan cupos registrar")
                        time.sleep(1)
                        lista_intentos=registro1.busca_boton(intento)
                        print(f'{lista_intentos}')
                        if lista_intentos!=None:
                            print("EXITO se registro el almuerzo intento")
                            cont = 1+cont
                            PaginaWeb.cerrar_pagina()
                            break
                print("no se registro el almuerzo")
                x,y=lista_intentos
            except Exception:
                try:
                    PaginaWeb.recargar_pagina()
                    time.sleep(1)
                    registro1=Registrador([".\sboton1.png",".\s2_0_boton_registrar1.png",".\s2_0_boton_registrar2.png",".\s2_0_boton_registrar3.png",".\s2_0_boton_registrar4.png",".\s2_0_boton_registrar5.png"])
                    for intento in registro1.imga:
                        Registrador.busca_con_comandos("registrar")
                        time.sleep(1)
                        lista_intentos=registro1.busca_boton(intento)
                        print(f'{lista_intentos}')
                        if lista_intentos!=None:
                            x,y = lista_intentos
                            break
                    time.sleep(1)
                    print(f'x,y = {x} , {y}')
                    pg.moveTo(x,y)
                    time.sleep(1)
                    pg.click(x,y)
                    time.sleep(1)    
                except Exception:
                    print("falla del sistema")
        
        with pg.hold("ctrl"):
            pg.press("tab")
            pg.press("tab")
    time.sleep(4)
    PaginaWeb.cerrar_pagina()
    time.sleep(10)
    PaginaWeb.cerrar_pagina()
    time.sleep(10)

    ##registrarPc.apagar_Pc()
"""
    while cont<=1:
        if cont ==1:
            link="https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062585"
            Sitio2.SitioWeb=link
        else:
            cont = cont+1

        while True:
            if abierto_chrome1 == False:
                abierto_chrome1=objeto1.abre_apliacion(".\google_abierto.png")
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
                        chrome2=objeto1.abre_apliacion(".\google_abierto.png")
                        abierto_pagina2=Sitio2.entra_pagina(abierto_chrome1)
                        while True: 
"""



                



    
