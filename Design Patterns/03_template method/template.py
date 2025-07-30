from random import randint
from abc import ABC, abstractmethod

class AlgorithimTemplate(ABC):
    def insert_data(self, data):
        formatted_data = self.__format_data(data)
        formatted_data_with_id = self.__insert_id(formatted_data)
        self.insert_value_in_doc(formatted_data_with_id)
        # This method can be overridden by subclasses if needed
        print(f"Inserting data: {formatted_data_with_id}")

    def __format_data(self, data):
        fomatted_data = {
            "nome": data[0],
            "sobrenome": data[1],
            "cidade": data[2]
        }
        return fomatted_data
    
    def __insert_id(self, formatted_data):
        formatted_data["id"] = randint(1, 1000)
        print(f"Data after inserting ID: {formatted_data}")
        return formatted_data
    
    @abstractmethod
    def insert_value_in_doc(self, formatted_data_with_id):
        # This method can be overridden by subclasses if needed
        pass

data = ["João", "Silva", "São Paulo"]
algorithimTemplate = AlgorithimTemplate()
algorithimTemplate.insert_data(data)