from abc import ABC, abstractmethod
#Interface é uma pré assinatura de uma classe abstrata, onde não é possível instanciar diretamente.
# Uma interface Trabalhador que define o comportamento básico de um trabalhador
# e uma classe Engenheiro que herda de Trabalhador e implementa os métodos trabalhar
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def horario_almoço(self) -> None:
        pass 

class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print("Engenheiro está trabalhando em um projeto.")

    def ir_para_casa(self) -> None:
        print("Engenheiro está indo para casa.")

    def horario_almoço(self) -> None:
        print("Engenheiro está em horário de almoço.")

class Programador(Trabalhador):
    def trabalhar(self) -> None:
        print("Programador está codificando.")

    def ir_para_casa(self) -> None:
        print("Programador está indo para casa.")

    def horario_almoço(self) -> None:
        print("Programador está em horário de almoço.")

# Exemplo de uso
def comunicar_trabalhador(trabalhador: Trabalhador) -> None:
    trabalhador.trabalhar()
    trabalhador.horario_almoço()
    trabalhador.ir_para_casa()

p1 = Engenheiro()
comunicar_trabalhador(p1)

p2 = Programador()
comunicar_trabalhador(p2)