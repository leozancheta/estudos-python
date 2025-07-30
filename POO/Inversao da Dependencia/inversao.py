from elemento import Elemento

class PrimeiroElemento(Elemento):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.__elem = Elemento(nome)
    
    def __str__(self):
        return f"Primeiro Elemento: {self.nome}"

    def get_elemento(self) -> Elemento:
        return self.__elem