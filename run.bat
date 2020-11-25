echo "Building the docker container..."
docker build -t conda-brooklyn .

echo "Startup yupiter..."
echo "Open a browser and navigate to http://localhost:8888"
docker run -it --rm -v %CD%:/opt/notebooks -p 8888:8888 conda-brooklyn