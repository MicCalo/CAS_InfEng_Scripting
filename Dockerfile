# Based on a recent anaconda with python 3.8
FROM continuumio/anaconda3:2020.07

# Load the required python libs
RUN pip install geopandas folium

# Create notebooks directroy
RUN mkdir /opt/notebooks

# Run yupiter server on port 8888 without any security (no password, no token).
# Use that container only locally on your machine.
CMD  /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root --NotebookApp.token=''
