### I M P O R T S 
from menu_class import *
from parsestr_class import *
from colorama import *



#
# F U N C I O N E S
#

def palindromos():
    # Ejemplo 1
    mi_cadena = ParseStr("Hola esto es una prueba")
    print("Frase de prueba 1 (" + str(len(mi_cadena)) + ") " +
          Fore.YELLOW + mi_cadena + Fore.WHITE)
    mostrar_resultado("Frase normalizada (" + # MOSTRAR RESULTADO ESTARA EN EL HELPERS
                      str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
    

###
# I N I C I O   P R O G R A M A
#

mi_menu = Menu("TAREAS ORIENTACION A OBJTOS")
mi_menu.addOption("Palindromos Object Oriented",
                  palindromos)


mi_menu.start()