#De La Huerta Avalos Gerardo Cristóbal
#2021630243
#6BM1


import pandas as pd

#hay que ajustar los pesos para obtener los and

weight1 = 0.5
weight2 = 0.5
bias = -1

test_inputs = [(0,0), (0,1), (1,0), (1,1)]
correct_outputs = [False, False, False, True]
outputs = []

for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

#para escribir resultados

num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns = ['input 1', 'input 2', 'linear conbination', 'Activation Output', 'Is Correct'])

if not num_wrong:
    print('Bien! Acertaste todas.\n')
else:
    print('Obtuviste {} mal. Debes poner otros pesos;\n'.format((num_wrong)))

print(output_frame.to_string(index=False))