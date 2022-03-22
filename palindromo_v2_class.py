# Como usar el método str.maketrans() .... https://www.w3schools.com/python/ref_string_maketrans.asp
# Que son y como usar métodos de clase ... https://ellibrodepython.com/metodos-estaticos-clase-python

# Versión con métodos de clase en lugar de métodos de instáncia

class Palindromo_V2(str):
    # ParseStr es un nuevo tipo de cadena que incluye normalización y test de palíndromo
    from_chars = "áàäâéèëêíìïîóòöôúùüû"
    to_chars = "aaaaeeeeiiiioooouuuu"
    eliminate_chars = ".-,:_'?¿()/&%$·!@¡`+* =ºª|#~€¬"
    translate_dictionary = str.maketrans(from_chars, to_chars, eliminate_chars)

    @classmethod
    def normalize(cls, cadena) -> str:
        normalized_str = str.lower(cadena)
        normalized_str = normalized_str.translate(cls.translate_dictionary)

        return normalized_str

    @classmethod
    def is_palindrome(cls, cadena) -> bool:
        normalized_str = cls.normalize(cadena)

        l = len(normalized_str)
        for idx in range(0, int(l/2)):
            if (normalized_str[idx] != normalized_str[-1*(idx+1)]):
                return False

        return True

