import numpy as np

weights = np.around(np.random.uniform(size=6) , decimals=2)

biases = np.around(np.random.uniform(size=3),decimals=2)



print(weights)
print(biases)


# input for x_1 , x_2

x_1 = 0.5
x_2 = 0.85

print('x1 is {} and x2 is {}'.format(x_1,x_2))

z_11 = x_1* weights[0] + x_2 * weights[1] + biases[0]

print('The weighted sum of the inputs at the first node in the hidden layer is {}'.format(z_11))

z_12 = x_1 * weights[0] + x_2 * weights[3] + biases [1]

print('The weighted sum of the inputs at the second node in the hidden layer is {}'.format(z_12))


'''Next, assuming a sigmoid activation function,
 let's compute the activation of the first node,  𝑎1,1
 , in the hidden layer.'''


a_11 = 1.0 / (1.0 + np.exp(-z_11))
print('The activation of the first node in the hidden layer is {}'.format(np.around(a_11, decimals=4)))

a_12 = 1.0 / (1.0 + np.exp(-z_12))
print('The activation of the first node in the hidden layer is {}'.format(np.around(a_12, decimals=4)))


z_2 = a_11 * weights[4] + a_12 * weights[5] + biases[2]

print('The weighted sum of the inputs at the node in the output layer is {}'.format(np.around(z_2, decimals=4)))

a_2 = 1.0 / (1.0 + np.exp(-z_2))
print('The activation of the first node in the output layer is {}'.format(np.around(a_2  , decimals=4)))




print('The output of the network for x1 = 0.5 and x2 = 0.85 is {}'.format(np.around(a_2, decimals=4)))




######################################################
'''In order to code an automatic way of making predictions'''
#####################################################

#Let's start by formally defining the structure of the network.

n = 2  # Number of inputs

num_hidden_layers = 2
m = [2,2] # number of nodes each hidden layer
num_nodes_output = 1 # number of nodes in the output layer

# initilazilize the weighrs and the biases


import numpy as np

n = 2  # Giriş katmanındaki düğüm sayısı
num_hidden_layers = 2  # Gizli katman sayısı
m = [2, 2]  # Her gizli katmandaki düğüm sayısı
num_nodes_output = 1  # Çıkış katmanındaki düğüm sayısı

num_nodes_previous = n
small_network = {}  # Ağırlıkları ve biasları depolamak için boş bir sözlük oluşturuluyor

# Her katman için döngüyü başlatın ve her düğümle ilişkilendirilmiş rastgele ağırlıkları ve biasları başlatın
# Çıkış katmanını dahil etmek için gizli katman sayısına 1 ekleyin

for layer in range(num_hidden_layers + 1):  # range(num_hidden_layers + 1) [0, 1, 2] için döngü oluşturur
    if layer == num_hidden_layers:
        # Çıkış katmanı
        layer_name = 'output'
        num_nodes = num_nodes_output
    else:
        # Gizli katmanlar
        layer_name = f'layer_{layer + 1}'
        num_nodes = m[layer]

    small_network[layer_name] = {}  # Her katman için bir sözlük oluşturuluyor

    for node in range(num_nodes):
        node_name = f'node_{node + 1}'  # 'node_1', 'node_2', ... gibi düğüm adları
        small_network[layer_name][node_name] = {
            'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
            'bias': np.around(np.random.uniform(size=1), decimals=2),
        }

    num_nodes_previous = num_nodes  # Sonraki katman için önceki düğüm sayısını güncelleyin

print(small_network)



####################################
# Fonks format
###################################

def initialize_network(num_inputs, num_hidden_layers, num_nodes_hidden, num_nodes_output):
    num_nodes_previous = num_inputs  # number of nodes in the previous layer

    network = {}

    # loop through each layer and randomly initialize the weights and biases associated with each layer
    for layer in range(num_hidden_layers + 1):

        if layer == num_hidden_layers:
            layer_name = 'output'  # name last layer in the network output
            num_nodes = num_nodes_output
        else:
            layer_name = 'layer_{}'.format(layer + 1)  # otherwise give the layer a number
            num_nodes = num_nodes_hidden[layer]

            # initialize weights and bias for each node
        network[layer_name] = {}
        for node in range(num_nodes):
            node_name = 'node_{}'.format(node + 1)
            network[layer_name][node_name] = {
                'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
                'bias': np.around(np.random.uniform(size=1), decimals=2),
            }

        num_nodes_previous = num_nodes

    return network  # return the network


'''
Use the initialize_network function to create a network that:
takes 5 inputs
has three hidden layers
has 3 nodes in the first layer, 2 nodes in the second layer, and 3 nodes in the third layer
has 1 node in the output layer
Call the network small_network.
'''
small_network = initialize_network(5, 3, [3, 2, 3], 3, )






## Forward Propagation

import numpy as np


def initialize_network(num_inputs, num_hidden_layers, num_nodes_per_layer, num_outputs):
    network = {}
    num_nodes_previous = num_inputs

    for layer in range(num_hidden_layers + 1):
        if layer == num_hidden_layers:
            layer_name = 'output'
            num_nodes = num_outputs
        else:
            layer_name = f'layer_{layer + 1}'
            num_nodes = num_nodes_per_layer[layer]

        network[layer_name] = {}

        for node in range(num_nodes):
            node_name = f'node_{node + 1}'
            network[layer_name][node_name] = {
                'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
                'bias': np.around(np.random.uniform(size=1), decimals=2),
            }

        num_nodes_previous = num_nodes

    return network


def compute_weighted_sum(inputs, weights, bias):
    return np.dot(inputs, weights) + bias


def node_activation(weighted_sum):
    return 1.0 / (1.0 + np.exp(-weighted_sum))


def forward_propagate(network, inputs):
    layer_inputs = list(inputs)  # start with the input layer as the input to the first hidden layer

    for layer in network:
        layer_data = network[layer]
        layer_outputs = []

        for layer_node in layer_data:
            node_data = layer_data[layer_node]
            weighted_sum = compute_weighted_sum(layer_inputs, node_data['weights'], node_data['bias'])
            node_output = node_activation(weighted_sum)
            layer_outputs.append(np.around(node_output[0], decimals=4))

        if layer != 'output':
            print(f'The outputs of the nodes in hidden layer number {layer.split("_")[1]} are: {layer_outputs}')

        layer_inputs = layer_outputs  # set the output of this layer to be the input to the next layer

    network_predictions = layer_outputs
    return network_predictions


# Example usage:
my_network = initialize_network(5, 3, [2, 3, 2], 1)
inputs = np.around(np.random.uniform(size=5), decimals=2)
predictions = forward_propagate(my_network, inputs)
print(f'The predicted value by the network for the given input is: {np.around(predictions[0], decimals=4)}')


def compute_weighted_sum(inputs, weights, bias):
    return np.sum(inputs * weights) + bias




from random import seed
import numpy as np

np.random.seed(12)
inputs = np.around(np.random.uniform(size=5), decimals=2)

print('The inputs to the network are {}'.format(inputs))


node_weights = small_network['layer_1']['node_1']['weights']
node_bias = small_network['layer_1']['node_1']['bias']

weighted_sum = compute_weighted_sum(inputs, node_weights, node_bias)
print('The weighted sum at the first node in the hidden layer is {}'.format(np.around(weighted_sum[0], decimals=4)))




def node_activation(weighted_sum):
    return 1.0 / (1.0 + np.exp(-1 * weighted_sum))
node_output  = node_activation(compute_weighted_sum(inputs, node_weights, node_bias))
print('The output of the first node in the hidden layer is {}'.format(np.around(node_output[0], decimals=4)))


