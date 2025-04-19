"""
Tests for the SimpleFCN neural network implementation.
"""

import numpy as np
import pytest
import sys
import os

# Add the notebooks directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from notebooks.A_forward_propagation_exercise import SimpleFCN

def test_initialization():
    """Test that the network initializes with correct weights and biases."""
    model = SimpleFCN()
    
    # Test layer 1 parameters
    expected_W1 = np.array([[0.2, -0.4],
                           [0.7,  0.3]])
    expected_b1 = np.array([0.1, 0.0])
    assert np.array_equal(model.W1, expected_W1)
    assert np.array_equal(model.b1, expected_b1)
    
    # Test layer 2 parameters
    expected_W2 = np.array([[ 0.5, -0.3],
                           [-0.4,  0.6]])
    expected_b2 = np.array([0.0, 0.05])
    assert np.array_equal(model.W2, expected_W2)
    assert np.array_equal(model.b2, expected_b2)

def test_relu():
    """Test the ReLU activation function."""
    model = SimpleFCN()
    
    # Test with positive values
    z = np.array([1.0, 2.0, 3.0])
    expected = np.array([1.0, 2.0, 3.0])
    assert np.array_equal(model.relu(z), expected)
    
    # Test with negative values
    z = np.array([-1.0, -2.0, -3.0])
    expected = np.array([0.0, 0.0, 0.0])
    assert np.array_equal(model.relu(z), expected)
    
    # Test with mixed values
    z = np.array([-1.0, 0.0, 1.0])
    expected = np.array([0.0, 0.0, 1.0])
    assert np.array_equal(model.relu(z), expected)

def test_softmax():
    """Test the softmax activation function."""
    model = SimpleFCN()
    
    # Test with simple values
    z = np.array([1.0, 2.0])
    output = model.softmax(z)
    assert np.allclose(np.sum(output), 1.0)  # Should sum to 1
    assert np.all(output >= 0)  # All values should be non-negative
    assert np.all(output <= 1)  # All values should be <= 1
    
    # Test with negative values
    z = np.array([-1.0, -2.0])
    output = model.softmax(z)
    assert np.allclose(np.sum(output), 1.0)
    
    # Test with large values (stability check)
    z = np.array([1000.0, 1001.0])
    output = model.softmax(z)
    assert not np.any(np.isnan(output))  # Should not have NaN values
    assert np.allclose(np.sum(output), 1.0)

def test_linear_forward():
    """Test the linear forward propagation."""
    model = SimpleFCN()
    
    # Test with simple values
    x = np.array([1.0, 2.0])
    W = np.array([[1.0, 2.0],
                  [3.0, 4.0]])
    b = np.array([0.1, 0.2])
    
    expected = np.array([5.1, 11.2])  # [1*1 + 2*2 + 0.1, 1*3 + 2*4 + 0.2]
    output = model.linear_forward(W, x, b)
    assert np.allclose(output, expected)

def test_forward_pass():
    """Test the complete forward pass through the network."""
    model = SimpleFCN()
    
    # Test with example input
    x = np.array([1.0, 2.0])
    output = model.forward(x)
    
    # Check output properties
    assert output.shape == (2,)  # Should have 2 output units
    assert np.allclose(np.sum(output), 1.0)  # Should sum to 1
    assert np.all(output >= 0)  # All values should be non-negative
    assert np.all(output <= 1)  # All values should be <= 1
    
    # Test with another input
    x = np.array([-1.0, 0.5])
    output = model.forward(x)
    assert output.shape == (2,)
    assert np.allclose(np.sum(output), 1.0)

def test_forward_pass_values():
    """Test specific values from the forward pass."""
    model = SimpleFCN()
    
    # Test with input [1.0, 2.0]
    x = np.array([1.0, 2.0])
    output = model.forward(x)
    
    # Expected values from the notebook example
    expected_z1 = np.array([-0.5, 1.3])  # W1 @ x + b1
    expected_a1 = np.array([0.0, 1.3])   # ReLU(z1)
    expected_z2 = np.array([-0.39, 0.83])  # W2 @ a1 + b2
    expected_y = np.array([0.22793645, 0.77206355])  # softmax(z2)
    
    # Compute intermediate values
    z1 = model.linear_forward(model.W1, x, model.b1)
    a1 = model.relu(z1)
    z2 = model.linear_forward(model.W2, a1, model.b2)
    y = model.softmax(z2)
    
    # Compare with expected values
    assert np.allclose(z1, expected_z1, atol=1e-6)
    assert np.allclose(a1, expected_a1, atol=1e-6)
    assert np.allclose(z2, expected_z2, atol=1e-6)
    assert np.allclose(y, expected_y, atol=1e-6)
    assert np.allclose(output, expected_y, atol=1e-6) 