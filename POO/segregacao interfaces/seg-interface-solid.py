from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def conssultar_beneficios(self) -> None:
        pass
# No principio de solid, se uma classe não precisa de um método, ela não deve implementá-lo.
#Deve-se criar uma hierarquia de classes que separem as responsabilidades.
# Não há problema em criar uma nova classe com menos elementos 
class TrabalhadorTemporario(Trabalhador):
    @abstractmethod
    def trabalhar(self) -> None:
        print("Trabalhador temporário está realizando uma tarefa.")
    @abstractmethod
    def ir_para_casa(self) -> None:
        print("Trabalhador temporário está indo para casa.")

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("Professor está lecionando.")

    def ir_para_casa(self) -> None:
        print("Professor está indo para casa.")

    def conssultar_beneficios(self) -> None:
        print("Professor está consultando seus benefícios.")

class ProfessorSubstituto(TrabalhadorTemporario):
    def trabalhar(self) -> None:
        print("Professor substituto está lecionando.")

    def ir_para_casa(self) -> None:
        print("Professor substituto está indo para casa.")