# Como crear y escribir en archivos de texto ... https://j2logo.com/como-escribir-en-un-fichero-en-python/
# Gestion de excepciones con try ............... https://www.w3schools.com/python/python_try_except.asp
# Método destructor de objetos ................. https://es.acervolima.com/python-__delete__-vs-__del__/
# Modos de apertura de una archivo ............. https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
# Posicionarse en un archivo ................... https://pynative.com/python-file-seek/

from colorama import Fore
from helpers import mostrar_resultado


class Logger():
    def __init__(self, log_path, log_name) -> None:
        self.path = log_path
        self.name = log_name

        # Abrimos el archivo de log para añadir nuevas entradas
        # Con el modo "a" si no existe se crear
        try:
            self.log_file = open(self.path + self.name, 'a+')
        except:
            raise Exception(
                "CLASE Logger: No se ha podido ni abrir ni crear el archivo de log", self.path, self.name)

    def __del__(self) -> None:
        # Este método se invoca cuando una instancia ya no puede ser usada
        # De este modo cerramos el archivo cuando ya no vamos ha usarlo liberando recursos
        self.log_file.close()
        pass

    def show(self) -> None:
        print(Fore.WHITE + "- Start Log " +
              Fore.YELLOW, self.path + self.name, Fore.WHITE, "-")

        # Nos posicionamos al inicio del archivo
        self.log_file.seek(0)
        for line in self.log_file:
            print("   " + line, end="")

        print(Fore.WHITE + "- End Log -")


    def log(self, txt) -> None:
        
        try:
            self.log_file.write(txt+"\n")
        except:
            # Devolvemos un error a la capa superiorf

            raise Exception(
                "CLASE Logger: No se ha podido grabar en el archivo de log")
