from abc import ABC, abstractmethod
# Uma classe abstrata pode ser generica e não pode ser instanciada diretamente.]
# Uma classe abstrata Pessoa que define o comportamento básico de uma pessoa
# e uma classe Estudante que herda de Pessoa e implementa o método trabalhar.
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
    
    def correr(self):
        print(f"{self.nome} está correndo.")
    
    @abstractmethod #Isso sionifica que a classe Pessoa é abstrata e não pode ser instanciada diretamente
    def trabalhar(self):
        pass

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"{self.nome} está estudando para o curso de {self.curso}.")

    def trabalhar(self):
        print(f"{self.nome} está trabalhando como estagiário no curso de {self.curso}.")

estiudante = Estudante("João", 20, "Engenharia")
estiudante.apresentar()
estiudante.correr()
estiudante.estudar()
estiudante.trabalhar()