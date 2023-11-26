# ponderada6m8

## Descrição do Projeto

A ponderada consiste no desenvolvimento de um perceptron e sua utilização para representar 4 portas lógicas (AND, OR, NAND e XOR). 

## Implementação

O perceptron foi implementado em Python, utilizando a biblioteca Numpy para facilitar a manipulação de vetores. O perceptron é uma classe que possui os seguintes métodos:

- `__init__(self, threshold, bias)`: Construtor da classe, recebe como parâmetros o threshold e o bias. O threshold é o valor que o perceptron deve atingir para que a saída seja 1, o bias é um valor que é somado ao resultado da função de ativação, para que o perceptron possa representar funções que não passam pela origem. O bias é opcional, por padrão é 0.
- `training(self, inputs, answers, learning_rate, rounds)`: Método que realiza o treinamento do perceptron. Recebe como parâmetros os inputs, answer, learning_rate e rounds. Os inputs são os valores de entrada, as answer são os valores esperados para cada entrada, o learning_rate é o valor que define o quão rápido o perceptron irá aprender, e o rounds é o número de vezes que o perceptron irá treinar.
- `predict(self, inputs)`: Método que recebe como parâmetro os inputs e retorna a saída do perceptron.

## Resultados

Os resultados obtidos foram os seguintes:

- AND:
  - Inputs: [[0, 0], [0, 1], [1, 0], [1, 1]]
  - Answers: [0, 0, 0, 1]
  - Threshold: 1
  - Bias: -1
  - Learning Rate: 0.1
  - Rounds: 100
  - Result: [0, 0, 0, 1]

- OR:
- Inputs: [[0, 0], [0, 1], [1, 0], [1, 1]]
  - Answers: [0, 1, 1, 1]
  - Threshold: 1
  - Bias: 0
  - Learning Rate: 0.1
  - Rounds: 100
  - Result: [0, 1, 1, 1]
- NAND:
  - Inputs: [[0, 0], [0, 1], [1, 0], [1, 1]]
  - Answers: [1, 1, 1, 0]
  - Threshold: 1
  - Bias: 1
  - Learning Rate: 0.1
  - Rounds: 100
  - Result: [1, 1, 1, 0]
- XOR:
- Inputs: [[0, 0], [0, 1], [1, 0], [1, 1]]
  - Answers: [0, 1, 1, 0]
  - Threshold: 1
  - Bias: 0
  - Learning Rate: 0.1
  - Rounds: 100
  - Result: [1, 0, 0, 0]

## Conclusão

O preceptron foi capaz de representar os valores esperados para as portas lógicas AND, OR e NAND, porém não foi capaz de representar a porta lógica XOR. Isso ocorre pois o perceptron é um classificador linear, e a porta lógica XOR não é linearmente separável. Para que o perceptron seja capaz de representar a porta lógica XOR, é necessário que ele possua mais de uma camada, ou seja, que seja uma rede neural.
