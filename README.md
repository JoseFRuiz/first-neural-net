# Building Your First Neural Network in Python

This repository provides a hands-on introduction to implementing neural networks from scratch in Python. It includes Jupyter notebooks with detailed explanations and exercises to help you understand the fundamentals of neural networks.

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [Prerequisites](#prerequisites)
3. [Installation & Setup](#installation--setup)
4. [Notebooks](#notebooks)
5. [Exercise Validation](#exercise-validation)
6. [Customizing Dependencies](#customizing-dependencies)
7. [Contributing](#contributing)
8. [License](#license)

## Repository Structure

```bash
first-neural-net/
├── Dockerfile           # Defines the Docker image
├── requirements.txt     # Python dependencies
├── notebooks/           # Jupyter notebooks
│   ├── A_forward_propagation.ipynb  # Forward propagation implementation
│   ├── utils.py         # Utility functions for visualization
│   ├── A_forward_propagation_exercise.py # Exercise implementation
│   └── exercise_validator.py  # Exercise validation utilities
├── tests/               # Unit tests
│   └── test_A_forward_propagation_exercise.py  # Tests for A_forward_propagation_exercise.py implementation
└── README.md            # This file
```

## Prerequisites

- **Docker (version ≥ 19.03)**: install from https://www.docker.com/
  - On **Linux**, verify the Docker daemon (`dockerd`) is running (e.g., `sudo systemctl status docker`).
  - On **Windows/macOS**, ensure Docker Desktop is installed and running (look for the Docker icon in your status bar).
- Git: used to clone the repository (`git clone`).
- A web browser: required to access the Jupyter Lab interface.

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/JoseFRuiz/first-neural-net.git
cd first-neural-net
```

### Build the Docker Image

From within the project root:

```bash
docker build -t neural-net .
```

- `-t neural-net` tags the image as `neural-net`.
- You can replace `neural-net` with any name you prefer.

### Run the Docker Container

To start Jupyter Lab on port 8888 with volume mounting for persistent changes:

```bash
docker run --rm -p 8888:8888 -v "$(pwd)/notebooks:/home/jovyan/work:rw" neural-net
```

After running this command, open your web browser and navigate to:
```
http://localhost:8888
```

This will open Jupyter Lab, where you can work with the notebooks and run your code.

## Notebooks

The repository contains the following notebooks:

1. **A_forward_propagation.ipynb**
   - Implements forward propagation through a simple neural network
   - Covers key concepts: linear transformations, ReLU activation, and softmax
   - Includes hands-on exercises with validation
   - 💡 *Bonus section*: Extend the implementation to support batch inputs using class inheritance

## Exercise Validation

The `exercise_validator.py` module provides functions to validate your solutions to exercises. You can evaluate your implementation in two ways:

1. **Using the Notebook**:
   Run the validation cells in `A_forward_propagation.ipynb` which will test your implementation using the built-in validator:
   ```python
   from exercise_validator import test_linear_forward, test_relu, test_softmax, test_forward
   
   # Run all tests
   test_linear_forward(model)
   test_relu(model)
   test_softmax(model)
   test_forward(model)
   ```

2. **Using pytest**:
   Complete the methods in `A_forward_propagation_exercise.py`. Then run the tests from within the Docker container:
   ```bash
   # Start the container with an interactive shell
   docker run -it --rm -v "$(pwd):/home/jovyan/work" neural-net /bin/bash
   
   # Navigate to the project directory
   cd /home/jovyan/work
   
   # Run the tests
   pytest tests/test_A_forward_propagation_exercise.py -v
   ```
   
   The tests will verify:
   - Correct initialization of weights and biases
   - ReLU activation function behavior
   - Softmax activation function properties
   - Linear forward propagation
   - Complete forward pass through the network
   - Specific values from the example in the notebook


## Customizing Dependencies

The project uses the following main dependencies:
- numpy: For numerical computations
- matplotlib: For visualization
- jupyterlab: For the development environment

To add additional dependencies:
1. Edit `requirements.txt`
2. Rebuild the Docker image:
   ```bash
   docker build -t neural-net .
   ```

## Contributing

1. Fork this repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
