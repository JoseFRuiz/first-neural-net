# Building your first neural network in python

This repository provides a Docker‑packaged Jupyter Lab environment for developing and sharing Jupyter notebooks with minimal setup. Anyone can clone this repo, build the Docker image, and launch a ready‑to‑use Jupyter Lab server.

---

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [Prerequisites](#prerequisites)
3. [Installation & Setup](#installation--setup)
   - [Clone the Repository](#clone-the-repository)
   - [Build the Docker Image](#build-the-docker-image)
   - [Run the Docker Container](#run-the-docker-container)
4. [Using Jupyter Lab](#using-jupyter-lab)
5. [Working with Notebooks](#working-with-notebooks)
6. [Customizing Dependencies](#customizing-dependencies)
7. [Mounting Local Directories (Optional)](#mounting-local-directories-optional)
8. [Advanced Configuration](#advanced-configuration)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)

---

## Repository Structure

```bash
my-notebook-project/
├── Dockerfile           # Defines the Docker image
├── requirements.txt     # Python dependencies
├── notebooks/           # Your Jupyter notebooks go here
│   └── example.ipynb
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
git clone https://github.com/<your-username>/my-notebook-project.git
cd my-notebook-project
```


### Build the Docker Image

From within the project root:

```bash
docker build -t my-notebook .
```

- `-t my-notebook` tags the image as `my-notebook`.
- You can replace `my-notebook` with any name you prefer.


### Run the Docker Container

To start Jupyter Lab on port 8888:

```bash
docker run --rm -p 8888:8888 my-notebook
```

- `--rm` automatically removes the container when stopped.
- `-p 8888:8888` maps container port 8888 to localhost:8888.


## Using Jupyter Lab

1. After running the container, open your browser to:

   ```text
   http://localhost:8888
   ```

2. No token or password is required (configured in the Dockerfile).
3. Explore the file browser — you should see the `example.ipynb` notebook in `work/`.


## Working with Notebooks

- Place any new or existing `.ipynb` files into the `notebooks/` directory.
- Rebuild the Docker image (or mount a volume) to have them appear in Jupyter Lab.


## Customizing Dependencies

If your notebooks require additional Python packages:

1. Open `requirements.txt`.
2. Add one package per line, e.g.:
   ```text
   numpy
   pandas
   matplotlib
   ```
3. Rebuild the image:
   ```bash
   docker build -t my-notebook .
   ```

## Mounting Local Directories (Optional)

Rather than rebuilding for every change, you can mount your local `notebooks/`:

```bash
docker run --rm -p 8888:8888 \
  -v "$(pwd)/notebooks:/home/jovyan/work" \
  my-notebook
```

- Changes in your local `notebooks/` folder will instantly reflect in the container.


## Advanced Configuration

- To enable GPU support, switch to a CUDA‑enabled base image (e.g., `jupyter/cuda-notebook`) and install any GPU libraries in the Dockerfile.
- To set a custom Jupyter Lab password, modify the `CMD` in the Dockerfile:
  ```dockerfile
  CMD ["start.sh", "jupyter", "lab", \
       "--LabApp.password='sha1:...'", \
       "--LabApp.ip=0.0.0.0"]
  ```


## Troubleshooting

- **Port already in use**: Change the host port (e.g., `-p 9999:8888`) and visit `http://localhost:9999`.
- **Permission errors on notebooks**: Ensure files in `notebooks/` are readable by UID 1000 (the `jovyan` user).
- **Docker daemon not running**: Start Docker Desktop or run `sudo systemctl start docker`.


## Contributing

1. Fork this repo.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes and push: `git push origin feature/your-feature`.
4. Open a Pull Request.


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
