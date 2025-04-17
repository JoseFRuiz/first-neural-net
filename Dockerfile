# Use the official minimal Jupyter base image
FROM jupyter/base-notebook:latest

# Switch to root to install any extra OS packages if needed
USER root
# (Optional) e.g., RUN apt-get update && apt-get install -y git

# Switch back to jovyan and install Python deps
USER $NB_UID
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy your notebooks into the container
COPY notebooks/ /home/jovyan/work/

WORKDIR /home/jovyan/work

# Expose Jupyter port
EXPOSE 8888

# Start JupyterLab without a token
CMD ["start.sh", "jupyter", "lab", "--LabApp.token=''", "--LabApp.allow_origin='*'", "--LabApp.ip=0.0.0.0"]
