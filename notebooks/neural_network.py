"""
Implementation of a simple fully connected neural network.

This module contains the SimpleFCN class that implements a two-layer neural network
with ReLU activation in the hidden layer and softmax activation in the output layer.
"""

import numpy as np

class SimpleFCN:
    def __init__(self):
        # Assign fixed weights and biases for layer 1
        self.W1 = None # TODO: Assign the weights for layer 1
        self.b1 = None # TODO: Assign the biases for layer 1

        # Assign fixed weights and biases for layer 2
        self.W2 = None # TODO: Assign the weights for layer 2
        self.b2 = None # TODO: Assign the biases for layer 2

    def relu(self, z):
        """
        Applies the ReLU function element-wise:
        ReLU(z_i) = max(0, z_i)
        """
        pass # TODO: Implement the ReLU function

    def softmax(self, z):
        """
        Converts raw scores into probabilities:
        z_hat = z - max(z) # stability trick
        softmax(z_hat_i) = exp(z_hat_i) / sum(exp(z_hat_j))
        """
        pass # TODO: Implement the softmax function

    def linear_forward(self, W, x, b):
        """
        Implements linear forward propagation: z = Wx + b
        Args:
            x: input vector (n,)
            W: weight matrix (m,n)
            b: bias vector (m,)
        Returns:
            z: output vector (m,)
        """
        pass # TODO: Implement the linear forward function

    def forward(self, x):
        # First layer
        z1 = None # TODO: First layer linear transformation
        a1 = None # TODO: First layer ReLU activation

        # Output layer
        z2 = None # TODO: Output layer linear transformation
        y = None # TODO: Output layer softmax activation
        return y
    
# Create the network
model = SimpleFCN()

# Define input vector
x = np.array([1.0, 2.0])

# Run forward pass
output = model.forward(x)
print("Output probabilities:", output)

# EXERCISE SOLUTION — NOT VISIBLE TO LEARNERS
# This cell contains the reference solution and validation.
# It should be used for instructor/testing purposes only.

# class SimpleFCN:
#     def __init__(self):
#         # Assign fixed weights and biases for layer 1
#         self.W1 = np.array([[0.2, -0.4],
#                            [0.7,  0.3]])
#         self.b1 = np.array([0.1, 0.0])

#         # Assign fixed weights and biases for layer 2
#         self.W2 = np.array([[ 0.5, -0.3],
#                            [-0.4,  0.6]])
#         self.b2 = np.array([0.0, 0.05])

#     def relu(self, z):
#         """
#         Applies the ReLU function element-wise:
#         ReLU(z_i) = max(0, z_i)
#         """
#         return np.maximum(0, z)

#     def softmax(self, z):
#         """
#         Converts raw scores into probabilities:
#         z_hat = z - max(z) # stability trick
#         softmax(z_hat_i) = exp(z_hat_i) / sum(exp(z_hat_j))
#         """
#         exp_z = np.exp(z - np.max(z))  # stability trick
#         return exp_z / np.sum(exp_z)

#     def linear_forward(self, W, x, b):
#         """
#         Implements linear forward propagation: z = Wx + b
#         Args:
#             x: input vector (n,)
#             W: weight matrix (m,n)
#             b: bias vector (m,)
#         Returns:
#             z: output vector (m,)
#         """
#         return np.dot(W, x) + b

#     def forward(self, x):
#         """
#         Performs forward propagation through the network.
#         Args:
#             x: input vector (2,)
#         Returns:
#             y: output probabilities (2,)
#         """
#         # First layer
#         z1 = self.linear_forward(self.W1, x, self.b1)
#         a1 = self.relu(z1)

#         # Output layer
#         z2 = self.linear_forward(self.W2, a1, self.b2)
#         y = self.softmax(z2)
#         return y 