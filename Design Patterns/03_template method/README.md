# Padrão de Design Template Method

## O que é o Template Method?

O Template Method é um padrão de design comportamental que define o esqueleto de um algoritmo na superclasse, mas permite que as subclasses substituam etapas específicas do algoritmo sem alterar sua estrutura.

## Propósito

O padrão Template Method é útil quando:
- Você quer permitir que clientes estendam apenas etapas particulares de um algoritmo, não o algoritmo inteiro
- Você tem várias classes que contêm algoritmos quase idênticos com algumas diferenças menores
- Você quer localizar o código comum entre várias classes em um único lugar para evitar duplicação

## Estrutura

A estrutura básica do padrão Template Method inclui:
- **Classe Abstrata**: Define operações primitivas (abstratas) que subclasses concretas devem implementar, e implementa um método de template que contém a estrutura do algoritmo
- **Classes Concretas**: Implementam as operações primitivas para realizar subetapas específicas do algoritmo

## Exemplo neste Projeto

Neste projeto, temos uma implementação do padrão Template Method em Python:

1. `template.py` - Contém a classe abstrata `TemplateMethod` que define a estrutura do algoritmo
2. `csv_processor.py` - Contém a classe concreta `CSVProcessor` que implementa etapas específicas do algoritmo para processamento de CSV

O método template (`insert_data()`) na classe abstrata define o fluxo de trabalho geral para inserir dados, enquanto cada subclasse implementa detalhes específicos como `insert_value_in_doc()`.

## Benefícios

- **Reutilização de código**: O código comum fica na superclasse, evitando duplicação
- **Extensibilidade**: Facilita a adição de novas variantes do algoritmo
- **Inversão de controle**: Implementa o princípio "Hollywood" ("não nos chame, nós chamaremos você"), onde a superclasse chama os métodos da subclasse quando necessário
- **Flexibilidade**: Permite variar apenas certas partes de um algoritmo grande

## Quando Usar

Use o padrão Template Method quando:
- Você quer implementar as partes invariáveis de um algoritmo uma vez e deixar as subclasses implementarem o comportamento que pode variar
- Você quer controlar em que pontos a herança pode ocorrer
- Você precisa centralizar código para evitar duplicação

O Template Method é um dos padrões fundamentais para reutilização de código e é muito utilizado em frameworks e bibliotecas.
