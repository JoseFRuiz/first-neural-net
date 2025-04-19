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
│   └── exercise_validator.py  # Exercise validation utilities
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
git clone https://github.com/<your-username>/first-neural-net.git
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

To start Jupyter Lab on port 8888 with volume mounting for persistent changes:

```bash
docker run --rm -p 8888:8888 \
  -v "$(pwd)/notebooks:/home/jovyan/work:rw" \
  neural-net
```

## Notebooks

The repository contains the following notebooks:

1. **A_forward_propagation.ipynb**
   - Implements forward propagation through a simple neural network
   - Covers key concepts: linear transformations, ReLU activation, and softmax
   - Includes hands-on exercises with validation

## Exercise Validation

The `exercise_validator.py` module provides functions to validate your solutions to exercises. For example:

```python
from exercise_validator import validate_nn_architecture

# Validate neural network architecture
is_valid, message = validate_nn_architecture([3, 5, 5, 2])
print(message)
```

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
