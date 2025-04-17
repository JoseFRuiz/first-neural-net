# Use the official minimal Jupyter base image
FROM jupyter/base-notebook:latest

# Switch to root to install any OS packages (if needed)
USER root
# e.g., RUN apt-get update && apt-get install -y git

# Copy notebooks and set correct ownership for jovyan
COPY --chown=1000:100 notebooks/ /home/jovyan/work/

# Switch back to the default non‑root user
USER $NB_UID

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Make sure we're in the working directory
WORKDIR /home/jovyan/work

# Expose Jupyter Lab port
EXPOSE 8888

# Launch Jupyter Lab without a token on all interfaces
CMD ["start.sh", "jupyter", "lab", \
     "--LabApp.token=''", \
     "--LabApp.allow_origin='*'", \
     "--LabApp.ip=0.0.0.0"]
