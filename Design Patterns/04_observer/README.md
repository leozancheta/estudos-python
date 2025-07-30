# Padrão de Design Observer

## O que é o Observer?

O Observer (Observador) é um padrão de design comportamental que define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

## Propósito

O padrão Observer é útil quando:
- Uma mudança em um objeto requer mudanças em outros objetos, e você não sabe quantos objetos precisam ser alterados
- Um objeto precisa notificar outros objetos sem fazer suposições sobre quem são esses objetos
- Você precisa manter baixo acoplamento entre objetos que interagem entre si

## Estrutura

A estrutura básica do padrão Observer inclui:
- **Subject (Assunto)**: Mantém uma lista de observadores e fornece métodos para adicionar ou remover observadores
- **Observer (Observador)**: Define uma interface de atualização para objetos que devem ser notificados de mudanças no Subject
- **ConcreteSubject (Assunto Concreto)**: Armazena o estado de interesse para os observadores e envia notificações quando o estado muda
- **ConcreteObserver (Observador Concreto)**: Mantém uma referência ao ConcreteSubject, implementa a interface Observer e mantém seu estado consistente com o do Subject

## Exemplos neste Projeto

Neste projeto, temos duas implementações do padrão Observer em Python:

1. **Implementação Básica** (`observer.py`):
   - Demonstra a estrutura fundamental do padrão Observer
   - Inclui classes `Subject`, `Observer`, `ConcreteObserverA` e `ConcreteObserverB`
   - Mostra como observadores podem reagir de maneira diferente às mudanças no estado do Subject

2. **Estação Meteorológica** (`weather_observer.py`):
   - Implementação mais prática do padrão Observer
   - `WeatherStation` atua como Subject, mantendo dados sobre temperatura, umidade e pressão
   - `DisplayDevice` e `WeatherAlert` são observadores que reagem às mudanças climáticas
   - Demonstra como o padrão pode ser usado em um cenário real

## Benefícios

- **Acoplamento Fraco**: Subjects e Observers podem interagir sem conhecimento detalhado um do outro
- **Suporte para Broadcast**: Permite enviar dados para todos os objetos interessados sem especificar os receptores
- **Flexibilidade Dinâmica**: Observadores podem ser adicionados e removidos em tempo de execução
- **Extensibilidade**: Novos tipos de observadores podem ser adicionados sem modificar o Subject

## Quando Usar

Use o padrão Observer quando:
- Uma abstração tem dois aspectos, um dependente do outro
- Uma mudança em um objeto requer mudanças em um número desconhecido de outros objetos
- Você precisa notificar outros objetos sem saber quem são esses objetos
- Você quer evitar acoplamento forte entre componentes do sistema

## Exemplos do Mundo Real

O padrão Observer é amplamente usado em:
- Interfaces gráficas (GUI) para notificar sobre eventos de usuário
- Sistemas de notificação em tempo real
- Frameworks de eventos em JavaScript (como React)
- Sistemas de publicação-assinatura
- Atualizações de feed em redes sociais

## Como Executar os Exemplos

Para executar os exemplos deste projeto, use os seguintes comandos:

```bash
# Exemplo básico do padrão Observer
python observer.py

# Exemplo da Estação Meteorológica
python weather_observer.py
```
