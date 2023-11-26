import numpy as np
class Perceptron:
    def __init__(self,threshold: int,bias :int) -> None:
      
        self.threshold =threshold
        self.bias = bias

    def predict(self,input:np.array):
        if len(input) != len(self.weights):
            raise Exception("input dimension invalid")
        value=self.bias +np.dot(input,self.weights)
        
        return int(value >= self.threshold)
    
    def training(self,inputs:np.array,answers: np.array,learning_rate:int,rounds=100):
        self.weights = np.zeros(len(inputs[0]))
        for round in range(rounds):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                self.weights += learning_rate * (answers[i] - prediction) * inputs[i]
                self.bias += learning_rate * (answers[i] - prediction)
                

    

# test perceptron for and gate
and_gate = Perceptron(1,0)
and_gate.training(np.array([[0,0],[0,1],[1,0],[1,1]]),np.array([0,0,0,1]),0.1)
print("and gate")
print(and_gate.predict(np.array([0,0])))
print(and_gate.predict(np.array([0,1])))
print(and_gate.predict(np.array([1,0])))
print(and_gate.predict(np.array([1,1])))
#test for or gate
or_gate = Perceptron(1,0)
or_gate.training(np.array([[0,0],[0,1],[1,0],[1,1]]),np.array([0,1,1,1]),0.1)
print("or gate")
print(or_gate.predict(np.array([0,0])))
print(or_gate.predict(np.array([0,1])))
print(or_gate.predict(np.array([1,0])))
print(or_gate.predict(np.array([1,1])))
#test for nand gate
nand_gate = Perceptron(1,2)
nand_gate.training(np.array([[0,0],[0,1],[1,0],[1,1]]),np.array([1,1,1,0]),0.1)
print("nand gate")
print(nand_gate.predict(np.array([0,0])))
print(nand_gate.predict(np.array([0,1])))
print(nand_gate.predict(np.array([1,0])))
print(nand_gate.predict(np.array([1,1])))
#test for xor gate
xor_gate = Perceptron(1,2)
xor_gate.training(np.array([[0,0],[0,1],[1,0],[1,1]]),np.array([0,1,1,0]),0.1)
print("xor gate")
print(xor_gate.predict(np.array([0,0])))
print(xor_gate.predict(np.array([0,1])))
print(xor_gate.predict(np.array([1,0])))
print(xor_gate.predict(np.array([1,1])))
