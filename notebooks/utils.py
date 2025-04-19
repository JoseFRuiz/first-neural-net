"""
Utility functions and classes for neural network implementation.

This module serves as a collection point for various utility functions and classes
that can be used across different parts of the neural network implementation.

Usage:
    from utils import <function_name>
"""

import matplotlib.pyplot as plt
from math import atan2, cos, sin


# The classes Neuron, Layer, and NeuralNetwork were adapted from the following source:
# https://stackoverflow.com/questions/29888233/how-to-visualize-a-neural-network


class Neuron:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self, r):
        circle = plt.Circle((self.x, self.y), radius=r, fill=False)
        plt.gca().add_patch(circle)

class Layer:
    def __init__(self, network, n_neurons, max_neurons):
        # spacing between layers (x‑axis) and between neurons (y‑axis)
        self.layer_spacing   = 6
        self.neuron_spacing  = 2
        self.neuron_radius   = 0.5

        self.prev = network.layers[-1] if network.layers else None
        # x‑position: 0 for first layer, otherwise prev.x + layer_spacing
        self.x = 0 if self.prev is None else self.prev.x + self.layer_spacing

        # build neurons vertically centered around y=0
        self.neurons = []
        start_y = - self.neuron_spacing*(n_neurons-1)/2
        for i in range(n_neurons):
            y = start_y + i*self.neuron_spacing
            self.neurons.append(Neuron(self.x, y))

    def _connect(self, a, b):
        dx, dy = b.x - a.x, b.y - a.y
        θ = atan2(dy, dx)
        xa, ya = self.neuron_radius*cos(θ), self.neuron_radius*sin(θ)
        line = plt.Line2D((a.x+xa, b.x-xa), (a.y+ya, b.y-ya))
        plt.gca().add_line(line)

    def draw(self, label=None):
        # draw neurons and connections from prev layer
        for n in self.neurons:
            n.draw(self.neuron_radius)
            if self.prev:
                for p in self.prev.neurons:
                    self._connect(p, n)

        # optional label above the top neuron
        if label:
            top_y = max(n.y for n in self.neurons)
            plt.text(self.x, top_y + self.neuron_spacing/2, label,
                     ha='center', fontsize=12)

class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.layers = []
        max_width = max(layer_sizes)
        for size in layer_sizes:
            layer = Layer(self, size, max_width)
            self.layers.append(layer)

    def draw(self):
        plt.figure(figsize=(len(self.layers)*2, 6))
        # draw each layer with an appropriate label
        for i, layer in enumerate(self.layers):
            if   i == 0:                lbl = 'Input'
            elif i == len(self.layers)-1: lbl = 'Output'
            else:                       lbl = f'Hidden {i}'
            layer.draw(label=lbl)

        # compute and set axis limits so nothing is clipped
        all_x = [n.x for L in self.layers for n in L.neurons]
        all_y = [n.y for L in self.layers for n in L.neurons]
        pad_x = (max(all_x)-min(all_x))*0.1
        pad_y = (max(all_y)-min(all_y))*0.1
        plt.xlim(min(all_x)-pad_x, max(all_x)+pad_x)
        plt.ylim(min(all_y)-pad_y, max(all_y)+pad_y)

        plt.axis('off')
        plt.axis('equal')
        plt.title('Neural Network (left → right)', fontsize=15)
        plt.show()