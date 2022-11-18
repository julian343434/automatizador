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
<<<<<<< HEAD
    time.sleep(5)
=======
    time.sleep(300)
>>>>>>> 4570115fe4ef0f58df690e6ca1b16a99db62cc90
    ## Termina la espera
    
    cont=0    
    objeto1 =Pc("chrome")
    Sitio1=PaginaWeb("https://siau.unillanos.edu.co:8443/ORION/Login")   
    s="deivid.hernandez"
    m="alex8604ALEX;:_"
    link="https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595"
    usiario1=Usuario(s,m)

    Sitio2= PaginaWeb(link)


    abierto_chrome1=False
    abierto_pagina1=False
    credenciales_entradas=False
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
                            try:
                                Registrador.busca_con_comandos("registrar")
                                registro1=Registrador(".\sboton1.png")
                                x, y =registro1.busca_boton(registro1.imga)
                                print(f'x,y = {x} , {y}')
                                pg.moveTo(x,y)
                                pg.click()
                                time.sleep("2")
                                with pg.hold("ctrl"):
                                    pg.press("r")
                                time.sleep("2")
                                Registrador.busca_con_comandos("exitoso")
                                time.sleep("2")
                                registro2=Registrador(".\Exitoso.png") 
                                z, w = registro2.busca_boton(registro2.imga)
                                time.sleep(5)
                                Sitio2.cerrar_pagina()
                                break 
                            except TypeError:
                                print("no se registro el almuerzo")
                                time.sleep(2)
                                with pg.hold("ctrl"):
                                    pg.press("r")      
    Pc.apagar_Pc() 




                



    
