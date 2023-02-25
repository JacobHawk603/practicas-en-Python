import numpy as np
import pandas as pd

def function_h(X, W, b):
    suma = np.dot(W, X) + b
    return suma

def sigmoid(x):
    sg = 1/(1+np.exp(x))
    return sg

def escalon(x):
    
    valor = 1 if x>=0 else 0
    return valor
    

if __name__ == "__main__":
    
    #definimos inputs y sesgo
    inputs = np.array([0.7, -0.3])
    weights = np.array([0.1, 0.8])
    bias = -0.1
    
    #pasada frontal
    h = function_h(inputs, weights, bias)
    output = sigmoid(h)
    
    print('Output:')
    print(output)
    
    #pruebas extra!!!-----------------------------------------
    
    test_inputs = [(0,0),(0,1),(1,0),(1,1)]
    correct_outputs = [False, True, True, True]
    test_weights = np.array([1,1])
    test_bias = -1
    outputs = []
    
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_conbination = function_h(test_input, test_weights, test_bias)
        output = int(linear_conbination >=0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_conbination, output, is_correct_string])
    
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    outputFrame = pd.DataFrame(outputs, columns=['Input 1', 'Input 2', 'Linear conbination', 'Activation Output', 'Is correct'])
    
    if not num_wrong:
        print('Bien! acertaste Todas\n')
    else:
        print('Obtuviste {} mal, Debes colocar otros pesos!\n'.format(num_wrong))
        
    
    print("Output escalon: ", escalon(h))
    
    print(outputFrame.to_string(index=False))