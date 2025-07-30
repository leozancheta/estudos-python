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

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("Professor está lecionando.")

    def ir_para_casa(self) -> None:
        print("Professor está indo para casa.")

    def conssultar_beneficios(self) -> None:
        print("Professor está consultando seus benefícios.")

class ProfessorSubstituto(Trabalhador):
    def trabalhar(self) -> None:
        print("Professor substituto está lecionando.")

    def ir_para_casa(self) -> None:
        print("Professor substituto está indo para casa.")