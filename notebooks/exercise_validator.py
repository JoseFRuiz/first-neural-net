"""
Exercise validation utilities for neural network implementation.

This module contains functions to validate solutions to various exercises
in the neural network implementation course.

Usage:
    from exercise_validator import validate_nn_architecture
"""

import numpy as np

def validate_nn_architecture(nn_dim, expected_architecture=[3, 5, 5, 2]):
    """
    Validates that the neural network architecture matches the expected configuration.
    
    Args:
        nn_dim: The neural network architecture to validate
        expected_architecture: The expected architecture [input, hidden1, hidden2, output]
        
    Returns:
        tuple: (bool, str) - (is_valid, message)
    """
    if not isinstance(nn_dim, list):
        return False, "❌ nn_dim should be a list"
    
    if len(nn_dim) != len(expected_architecture):
        return False, f"❌ Expected {len(expected_architecture)} layers, got {len(nn_dim)}"
    
    if nn_dim != expected_architecture:
        return False, f"❌ Expected architecture {expected_architecture}, got {nn_dim}"
    
    return True, "✅ Architecture matches the expected configuration!"


def test_linear_forward(model):
    print("🔍 Testing: linear_forward...")
    x = np.array([1.0, 2.0])
    W = np.array([[1.0, -1.0], [0.5, 2.0]])
    b = np.array([0.0, 1.0])
    result = model.linear_forward(W, x, b)
    
    expected = np.array([-1., 5.5])
    
    assert isinstance(result, np.ndarray), "❌ Output is not a NumPy array."
    assert result.shape == expected.shape, f"❌ Expected shape {expected.shape}, got {result.shape}"
    assert np.allclose(result, expected), f"❌ Incorrect values: expected {expected}, got {result}"
    print("✅ linear_forward passed!")


def test_relu(model):
    print("🔍 Testing: relu...")
    z = np.array([-1.0, 0.0, 2.5])
    result = model.relu(z)
    expected = np.array([0.0, 0.0, 2.5])
    
    assert np.allclose(result, expected), f"❌ ReLU failed: expected {expected}, got {result}"
    print("✅ relu passed!")


def test_softmax(model):
    print("🔍 Testing: softmax...")
    z = np.array([1.0, 2.0, 3.0])
    result = model.softmax(z)
    expected = np.exp(z) / np.sum(np.exp(z))
    
    assert np.allclose(result, expected, atol=1e-6), "❌ Softmax values are incorrect."
    assert np.isclose(np.sum(result), 1.0), "❌ Softmax output does not sum to 1."
    print("✅ softmax passed!")


def test_forward(model):
    print("🔍 Testing: forward_pass...")
    x = np.array([1.0, 2.0])
    output = model.forward(x)

    assert isinstance(output, np.ndarray), "❌ Output must be a NumPy array."
    assert output.shape == (2,), f"❌ Expected output shape (2,), got {output.shape}"
    assert np.isclose(np.sum(output), 1.0, atol=1e-6), "❌ Output probabilities must sum to 1."
    assert np.all(output >= 0), "❌ Output contains negative probabilities."
    print("✅ forward_pass passed!")