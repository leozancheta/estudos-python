class Subject:
    """
    O Subject mantém uma lista de seus observadores e notifica-os quando seu estado muda.
    """
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """
        Adiciona um observador à lista de observadores.
        """
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        """
        Remove um observador da lista de observadores.
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        """
        Notifica todos os observadores sobre uma mudança de estado.
        """
        for observer in self._observers:
            observer.update(self)
    
    @property
    def state(self):
        """
        Retorna o estado atual do Subject.
        """
        return self._state
    
    @state.setter
    def state(self, state):
        """
        Define o estado do Subject e notifica todos os observadores.
        """
        self._state = state
        self.notify()


class Observer:
    """
    Interface para todos os observadores que devem ser notificados de mudanças no Subject.
    """
    def update(self, subject):
        """
        Recebe uma atualização do Subject.
        """
        pass


class ConcreteObserverA(Observer):
    """
    Implementação concreta de um observador que reage às mudanças no estado do Subject.
    """
    def update(self, subject):
        if subject.state < 3:
            print("ConcreteObserverA: Reagindo ao evento (estado < 3)")


class ConcreteObserverB(Observer):
    """
    Outra implementação concreta de um observador com uma lógica diferente.
    """
    def update(self, subject):
        if subject.state >= 3:
            print("ConcreteObserverB: Reagindo ao evento (estado >= 3)")


# Exemplo de uso do padrão Observer
if __name__ == "__main__":
    # Criando um Subject
    subject = Subject()
    
    # Criando observadores
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    
    # Registrando observadores no Subject
    subject.attach(observer_a)
    subject.attach(observer_b)
    
    # Mudando o estado do Subject e notificando os observadores
    print("Mudando o estado para 2:")
    subject.state = 2
    
    print("\nMudando o estado para 5:")
    subject.state = 5
    
    # Removendo um observador
    subject.detach(observer_a)
    
    print("\nMudando o estado para 1 (após remover observer_a):")
    subject.state = 1
