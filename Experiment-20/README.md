# Experiment 20: Implement CI/CD Pipeline for Application Deployment

This experiment extends the backend from Experiment 16 and adds containerization plus a GitHub Actions pipeline for continuous integration and deployment validation.

## Goal
- Integrate CD pipeline in the testing backend from Experiment 16
- Create a Docker image and run the container
- Create a CD pipeline using GitHub Actions

## Project Files
- [app.py](app.py) - Flask backend
- [test_app.py](test_app.py) - Backend unit tests
- [requirements.txt](requirements.txt) - Python dependencies
- [Dockerfile](Dockerfile) - Docker image build instructions
- [.github/workflows/ci.yml](.github/workflows/ci.yml) - GitHub Actions pipeline

## Backend API
### Start application locally
```bash
python app.py
```

### Test backend
```bash
pytest -v
pytest test_app.py
pytest --cov=app --cov-report=term-missing --cov-report=html
```

## Docker Commands
### Build Docker image
```bash
docker build -t exp20-backend:latest .
```

### Run Docker container
```bash
docker run -d --name exp20-backend -p 5000:5000 exp20-backend:latest
```

### Verify container
```bash
docker ps
docker images
curl http://localhost:5000/
```

### Stop container
```bash
docker stop exp20-backend
docker rm exp20-backend
```

## GitHub Actions Workflow
The pipeline in [.github/workflows/ci.yml](.github/workflows/ci.yml) performs:
1. Backend unit tests using `pytest`
2. Docker image build
3. Docker container run
4. Health check using `curl`

## Screenshot Requirements
Include these screenshots in your submission:
- Docker image and running container in CLI
- GitHub Actions workflow success screen

## Notes
- The backend uses in-memory storage for student records.
- The workflow runs automatically on push, pull request, and manual dispatch.
- This folder is ready to be zipped with code and README for submission.
