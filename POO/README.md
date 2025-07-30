# Programação Orientada a Objetos (POO)

## O que é POO?

Programação Orientada a Objetos é um paradigma de programação baseado no conceito de "objetos", que podem conter dados (atributos) e procedimentos (métodos). A POO organiza o código em unidades reutilizáveis que modelam entidades do mundo real ou conceitos abstratos.

## Conceitos Fundamentais da POO

### 1. Classe

Uma classe é um "modelo" ou "planta" para criar objetos. Ela define os atributos e métodos que seus objetos terão.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def buzinar(self):
        print("Bi-bi!")
```

### 2. Objeto

Um objeto é uma instância de uma classe. É uma entidade concreta criada a partir do modelo definido pela classe.

```python
meu_carro = Carro("Toyota", "Corolla")  # Criando um objeto da classe Carro
meu_carro.buzinar()  # Chamando um método do objeto
```

### 3. Atributos

Atributos são variáveis que pertencem a um objeto ou classe. Eles representam as características ou propriedades do objeto.

```python
# Atributos do objeto meu_carro
print(meu_carro.marca)    # Toyota
print(meu_carro.modelo)   # Corolla
```

### 4. Métodos

Métodos são funções que pertencem a uma classe e definem o comportamento dos objetos dessa classe.

```python
# Método da classe Carro
meu_carro.buzinar()   # Imprime: "Bi-bi!"
```

### 5. Encapsulamento

Encapsulamento é o conceito de esconder os detalhes internos de um objeto e expor apenas o necessário. Em Python, convencionalmente usamos underscore (`_`) para indicar atributos "privados".

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular    # Público
        self._saldo = saldo       # "Privado" (por convenção)
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
    
    def ver_saldo(self):
        return self._saldo
```

### 6. Herança

Herança permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse). Isso promove a reutilização de código.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

class Cachorro(Animal):  # Cachorro herda de Animal
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):  # Gato herda de Animal
    def fazer_som(self):
        return "Miau!"
```

### 7. Polimorfismo

Polimorfismo permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum. Isso é possível quando as classes compartilham métodos com a mesma assinatura.

```python
def animal_som(animal):
    print(animal.fazer_som())

rex = Cachorro("Rex")
felix = Gato("Felix")

animal_som(rex)    # Imprime: "Au au!"
animal_som(felix)  # Imprime: "Miau!"
```

### 8. Abstração

Abstração é o conceito de simplificar objetos complexos selecionando apenas os aspectos relevantes para o contexto. Classes abstratas definem interfaces sem implementação completa.

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
```

### 9. Composição

Composição é quando um objeto contém outros objetos como partes de si mesmo. É uma relação "tem um".

```python
class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()  # Composição: Carro tem um Motor
    
    def ligar(self):
        print("Ligando o carro...")
        self.motor.ligar()
```

### 10. Agregação

Agregação é um tipo especial de composição onde um objeto pode existir independentemente do objeto que o contém. É uma relação "tem um" mais fraca.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # Agregação: Carrinho tem produtos
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
```

## Princípios SOLID

Os princípios SOLID são diretrizes para escrever código orientado a objetos mais compreensível, flexível e sustentável:

1. **S** - Princípio da Responsabilidade Única: Uma classe deve ter apenas uma razão para mudar
2. **O** - Princípio Aberto/Fechado: Classes devem estar abertas para extensão, mas fechadas para modificação
3. **L** - Princípio da Substituição de Liskov: Objetos de uma superclasse devem poder ser substituídos por objetos de uma subclasse sem afetar a integridade do programa
4. **I** - Princípio da Segregação de Interface: Muitas interfaces específicas são melhores que uma interface genérica
5. **D** - Princípio da Inversão de Dependência: Dependa de abstrações, não de implementações concretas

## Exemplos Práticos

Nos diretórios abaixo, você encontrará exemplos práticos de cada um desses conceitos:

- `agregacao/` - Exemplo de agregação entre classes
- `abstract/` - Exemplo de classes abstratas
- `interfaces/` - Exemplo de interfaces em Python
- `segregacao interfaces/` - Exemplo do princípio de segregação de interfaces
- `Inversao da Dependencia/` - Exemplo do princípio de inversão de dependência
