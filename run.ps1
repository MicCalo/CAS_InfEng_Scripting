Write-Host -ForegroundColor Yellow  "Building the docker container..."
docker build -t conda-brooklyn .

Write-Host -ForegroundColor Yellow  "Startup yupiter..."
Write-Host -ForegroundColor Yellow  "Open a browser and navigate to http://localhost:8888"
docker run -it --rm -v ${PWD}:/opt/notebooks -p 8888:8888 conda-brooklyn