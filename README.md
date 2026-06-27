# Hello Cloud API

A minimal, clean, and beginner-friendly FastAPI application designed as **Phase 1** of a hands-on learning roadmap for Cloud, DevOps, Docker, Kubernetes, GitHub Actions, and Amazon EKS.

---

## Project Overview

The **Hello Cloud API** is a simple Python web application built using the FastAPI framework. It exposes three essential endpoints designed to demonstrate key DevOps concepts, such as application health checks and version identification, which are critical when deploying services to cloud environments and Kubernetes.

---

## Folder Structure

```text
hello-cloud-api/
│
├── .github/
│   └── workflows/
│       └── docker-build.yml  # GitHub Actions workflow for Docker Build CI
│
├── app/
│   ├── __init__.py           # Marks the directory as a Python package
│   └── main.py               # Application entrypoint containing FastAPI routes
│
├── .dockerignore             # Excludes local dev files from Docker build context
├── .gitignore                # Prevents virtual environments & cache files from being tracked
├── Dockerfile                # Docker configuration file for containerizing the app
├── README.md                 # Documentation and setup instructions
└── requirements.txt          # Pinned application dependencies (FastAPI & Uvicorn)
```

---

## Installation & Setup

Follow these steps to run the application locally on your machine.

### Prerequisites

- **Python 3.9 or higher** installed on your system. You can check your version by running:
  ```bash
  python3 --version
  ```

### 1. Create a Virtual Environment

It is highly recommended to isolate project dependencies using a Python virtual environment.

Run the following command in the project root directory:

```bash
python3 -m venv .venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment depending on your operating system:

* **macOS and Linux:**
  ```bash
  source .venv/bin/activate
  ```
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

Once activated, your terminal prompt will be prefixed with `(.venv)`.

### 3. Install Dependencies

Install the required packages defined in `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running the Server

Start the local development server using **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

* `app.main:app` refers to the `app` instance inside the `main.py` file located in the `app/` folder.
* The `--reload` flag enables auto-reload, meaning the server will automatically restart when you make changes to the code.

The server will start running at: **`http://127.0.0.1:8000`**

---

## Testing the Endpoints

You can verify the endpoints are functioning by using your browser, an API client (like Postman), or your terminal.

### 1. Root Endpoint (`GET /`)
* **URL:** `http://127.0.0.1:8000/`
* **Response:**
  ```json
  {
    "message": "Hello Kubernetes"
  }
  ```
* **Testing Command:**
  ```bash
  curl http://127.0.0.1:8000/
  ```

### 2. Health Check Endpoint (`GET /health`)
* **URL:** `http://127.0.0.1:8000/health`
* **Response:**
  ```json
  {
    "status": "healthy"
  }
  ```
* **Testing Command:**
  ```bash
  curl http://127.0.0.1:8000/health
  ```

### 3. Version Endpoint (`GET /version`)
* **URL:** `http://127.0.0.1:8000/version`
* **Response:**
  ```json
  {
    "version": "1.0.0"
  }
  ```
* **Testing Command:**
  ```bash
  curl http://127.0.0.1:8000/version
  ```

---

## Swagger API Documentation

FastAPI automatically generates interactive, self-documenting APIs.

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can use the Swagger UI to interactively test all endpoints directly from your browser.

---

## Docker Containerization (Phase 2)

You can containerize and run the application inside a Docker container using the following steps:

### Prerequisites
- Make sure you have **Docker** installed and running on your system.

### 1. Build the Docker Image

Run the following command in the project root directory (where the `Dockerfile` is located):

```bash
docker build -t hello-cloud-api:latest .
```

### 2. Run the Docker Container

Run the container in detached mode (`-d`), mapping port `8000` on your host to port `8000` in the container:

```bash
docker run -d -p 8000:8000 --name hello-cloud-api-container hello-cloud-api:latest
```

### 3. Verify the Containerized App

Test the containerized API endpoints:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
```

### 4. Stopping and Cleaning Up

To stop the running container:
```bash
docker stop hello-cloud-api-container
```

To remove the container:
```bash
docker rm hello-cloud-api-container
```

---

## CI/CD with GitHub Actions & Amazon ECR (Phase 3 & 4)

We have configured a CI/CD workflow that automatically builds the Docker image and pushes it to your Amazon Elastic Container Registry (ECR) on every push to the `main` branch.

### Prerequisites

To make the push succeed, you must add the following **GitHub Secrets** under your repository settings (`Settings > Secrets and variables > Actions`):

| Secret Name | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | Your AWS IAM User access key |
| `AWS_SECRET_ACCESS_KEY` | Your AWS IAM User secret key |
| `AWS_REGION` | Your target AWS Region (e.g. `us-east-1`) |
| `AWS_ACCOUNT_ID` | Your 12-digit AWS Account ID |
| `ECR_REPOSITORY` | The name of your Amazon ECR Repository |

### Workflow Configuration
The workflow file is located at [docker-build.yml](file:///Users/aayushsupe/Desktop/hello-cloud-api/.github/workflows/docker-build.yml) and performs the following tasks:
1. **Trigger**: Triggers on every push to the `main` branch.
2. **Environment**: Runs on the latest Ubuntu runner (`ubuntu-latest`).
3. **Steps**:
   - Checks out the project code.
   - Configures AWS credentials using your secrets.
   - Logs in to your Amazon ECR registry.
   - Builds the Docker image locally.
   - Tags the image to target your Amazon ECR registry.
   - Pushes the image to your ECR repository.



