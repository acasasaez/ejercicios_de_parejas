### I M P O R T S 
from menu_class import *
from palindromo_v1_class import *
from colorama import *
from helpers import *
from palindromo_v2_class import *

#
# F U N C I O N E S
#

def palindromos_instancia():
      # Ejemplo 1
      mi_cadena = Palindromo_V1("Hola esto es una prueba")
      print("Frase de prueba 1 (" + str(len(mi_cadena)) + ") " +
            Fore.YELLOW + mi_cadena + Fore.WHITE)
      mostrar_resultado("Frase normalizada (" +
                        str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
      mostrar_resultado("Es palindromo",
                        mi_cadena.is_palindrome())
      print()

      # Ejemplo 2
      mi_cadena = Palindromo_V1("Logré ver gol")
      print("Frase de prueba 2 (" + str(len(mi_cadena)) + ") " +
            Fore.YELLOW + mi_cadena + Fore.WHITE)
      mostrar_resultado("Frase normalizada (" +
                        str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
      mostrar_resultado("Es palindromo (iterativo", 
                        mi_cadena.is_palindrome())
      print()

      # Ejemplo 3
      mi_cadena = Palindromo_V1("Dábale arroz a la zorra el abad")
      print("Frase de prueba 3 (" + str(len(mi_cadena)) + ") " +
            Fore.YELLOW + mi_cadena + Fore.WHITE)
      mostrar_resultado("Frase normalizada (" +
                        str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
      mostrar_resultado("Es palindromo",
                        mi_cadena.is_palindrome())

def palindromos_clase():
      # Ejemplo 1
      mi_cadena = "Hola esto es una prueba"
      print("Frase de prueba 1 (" + str(len(mi_cadena)) + ") " +
            Fore.YELLOW + mi_cadena + Fore.WHITE)

      cadena_normalizada = Palindromo_V2.normalize(mi_cadena)
      mostrar_resultado("Frase normalizada (" +
                        str(len(cadena_normalizada)) + ") ",  cadena_normalizada)
      mostrar_resultado("Es palindromo",
                        Palindromo_V2.is_palindrome(mi_cadena))
      print()

      # Ejemplo 2
      mi_cadena = "Logré ver gol"
      print("Frase de prueba 2 (" + str(len(mi_cadena)) + ") " +
            Fore.YELLOW + mi_cadena + Fore.WHITE)
      cadena_normalizada = Palindromo_V2.normalize(mi_cadena)
      mostrar_resultado("Frase normalizada (" +
                        str(len(cadena_normalizada)) + ") ",  cadena_normalizada)
      mostrar_resultado("Es palindromo",
                        Palindromo_V2.is_palindrome(mi_cadena))

      print()

      # Ejemplo 3
      mi_cadena = "Dábale arroz a la zorra el abad"
      print("Frase de prueba 3 (" + str(len(mi_cadena)) + ") " +
            Fore.YELLOW + mi_cadena + Fore.WHITE)
      cadena_normalizada = Palindromo_V2.normalize(mi_cadena)
      mostrar_resultado("Frase normalizada (" +
                        str(len(cadena_normalizada)) + ") ",  cadena_normalizada)
      mostrar_resultado("Es palindromo",
                        Palindromo_V2.is_palindrome(mi_cadena))



###
# I N I C I O   P R O G R A M A
#
helpers.clear()   #Limpia la terminal
mi_menu = Menu("TAREAS ORIENTACION A OBJTOS")
mi_menu.addOption("Palindromo con métodos de instáncia", palindromos_instancia)
mi_menu.addOption("Palindromo con métodos de clase", palindromos_clase)


mi_menu.start()