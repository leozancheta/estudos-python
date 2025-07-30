# Padrão de Design Facade

## O que é o Facade?

O Facade (Fachada) é um padrão de design estrutural que fornece uma interface simplificada para um conjunto de interfaces em um subsistema. Ele define uma interface de nível mais alto que torna o subsistema mais fácil de usar, ocultando sua complexidade.

## Propósito

O padrão Facade é útil quando:
- Você precisa fornecer uma interface simples para um subsistema complexo
- Você quer desacoplar seu código de um sistema complexo
- Você quer organizar um sistema em camadas, usando facades como pontos de entrada para cada nível

## Estrutura

A estrutura básica do padrão Facade inclui:
- **Facade**: Fornece acesso simplificado às funcionalidades do subsistema
- **Subsistema**: Classes que implementam a funcionalidade do subsistema
- **Cliente**: Usa a Facade em vez de acessar diretamente o subsistema

## Exemplo neste Projeto

Neste projeto, temos uma implementação do padrão Facade em Python:

1. `facade.py` - Contém a classe `ImplementsNumpy` que atua como uma fachada para a biblioteca NumPy
2. `run.py` - Código cliente que utiliza a fachada para realizar operações estatísticas

A classe `ImplementsNumpy` serve como uma interface simplificada para operações comuns do NumPy, como criar arrays, calcular média, desvio padrão e soma, sem que o cliente precise conhecer a complexidade interna da biblioteca NumPy.

```python
# Exemplo de uso da fachada
data = [1, 2, 3, 4, 5]
numpy_impl = ImplementsNumpy()
array = numpy_impl.criar_array(data)
print("Média:", numpy_impl.media(array))
```

## Benefícios

- **Simplificação**: Esconde a complexidade do sistema e fornece uma interface mais simples
- **Desacoplamento**: Reduz a dependência entre o cliente e os subsistemas
- **Encapsulamento**: Encapsula um sistema complexo com uma interface mais amigável
- **Camadas**: Ajuda a estruturar sistemas em camadas e gerenciar dependências

## Quando Usar

Use o padrão Facade quando:
- Um sistema é muito complexo ou difícil de entender
- Você quer fornecer uma interface simplificada para um subsistema
- Você precisa desacoplar subsistemas de clientes e outros subsistemas
- Você quer dividir seu sistema em camadas

O Facade é especialmente útil quando se trabalha com bibliotecas de terceiros, frameworks ou qualquer código complexo que não se deseja expor diretamente aos clientes.
