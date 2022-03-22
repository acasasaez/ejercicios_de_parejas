# Como usar el método str.maketrans() .... https://www.w3schools.com/python/ref_string_maketrans.asp

class Palindromo_V1(str):
    # ParseStr es un nuevo tipo de cadena que incluye normalización y test de palíndromo
    from_chars = "áàäâéèëêíìïîóòöôúùüû"
    to_chars = "aaaaeeeeiiiioooouuuu"
    eliminate_chars = ".-,:_'?¿()/&%$·!@¡`+* =ºª|#~€¬"
    translate_dictionary = {}

    normalized_str = ""

    def __init__(self, string) -> None:
        super().__init__()
        self.translate_dictionary = \
            str.maketrans(self.from_chars, self.to_chars, self.eliminate_chars)

        self.__normalize()

    def __normalize(self) -> None:
        self.normalized_str = str.lower(self)
        self.normalized_str = self.normalized_str.translate(
            self.translate_dictionary)

    def is_palindrome(self) -> bool:
        l = len(self.normalized_str)
        for idx in range(0, int(l/2)):
            if (self.normalized_str[idx]!=self.normalized_str[-1*(idx+1)]):
                return False

        return True