# Padrão de Design Adapter

## O que é o Adapter?

O Adapter é um padrão de design estrutural que permite que objetos com interfaces incompatíveis trabalhem juntos. Ele atua como uma ponte entre duas interfaces incompatíveis, convertendo a interface de uma classe em outra interface que um cliente espera.

## Propósito

O padrão Adapter é útil quando:
- Você quer usar uma classe existente, mas sua interface não corresponde à que você precisa
- Você quer criar uma classe reutilizável que coopere com classes não relacionadas ou imprevistas
- Você precisa usar várias subclasses existentes, mas adaptar todas elas através de uma interface comum

## Estrutura

A estrutura básica do padrão Adapter inclui:
- **Cliente**: Colabora com objetos que aderem a uma interface específica
- **Interface Alvo**: Define a interface específica que o Cliente usa
- **Adaptador**: Adapta a interface da classe Adaptada para a interface Alvo
- **Adaptado**: Define uma interface existente que precisa ser adaptada

## Exemplo neste Projeto

Neste projeto, temos uma implementação do padrão Adapter em Python:

1. `adapter.py` - Contém a função `request_adapter` que adapta diferentes tipos de requisições HTTP (como Sanic e Flask) para um formato padrão
2. `fun_flask.py` - Implementação usando Flask
3. `run_sanic.py` - Implementação usando Sanic

O adaptador permite que o mesmo código funcione com diferentes frameworks web (Flask e Sanic), padronizando o formato das requisições.

## Benefícios

- **Reutilização de código**: Permite usar código existente mesmo quando não corresponde à interface necessária
- **Separação de preocupações**: Separa a lógica de negócios da lógica de interface
- **Flexibilidade**: Facilita a integração de novos frameworks ou bibliotecas no futuro

## Quando Usar

Use o padrão Adapter quando precisa fazer sistemas existentes funcionarem juntos sem modificar seu código fonte original, especialmente quando estiver lidando com bibliotecas ou frameworks de terceiros.
