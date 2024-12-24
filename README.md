# Dev-Ops-vigenere-cipher
A Dev Ops project made in colaboration with: https://github.com/aRowOf5

## Introduction

DevOps-vigenere-cipher project is a Flask-based web application that encrypts and decrypts files using the Vigenère cipher. The project utilizes Flask for the backend, Docker for
containerization, GitHub Actions for Continuous Integration/Continuous
Deployment (CI/CD) and Minikube (Local Kubernetes enviroment) to deploy.

## Technologies

* __Python__
* __Flask:__ A lightweight Python web framework.
* __GitHub Actions:__ A CI/CD platform integrated with GitHub repositories.
* __SonarCloud:__ A cloud-based code quality and security analysis tool.
* __Snyk:__ A security platform that helps find and fix vulnerabilities in dependencies.
* __Trivy:__ A simple and comprehensive vulnerability scanner for containers.
* __Docker:__ A platform for automating application deployment and managing
 containerized applications.
* __Minikube:__ Tool to run a single Kubernetes cluster locally on the computer
  
## Structure

The project structure is the typical Flask application structure with GitHub
Actions workflow files and Docker configuration.

## CI/CD Pipeline

### Stage 1: Style Checks

* __CheckCodeStyle:__ ensures that the code adheres to predefined style
  guidelines and standards, maintaining consistency and readability across the codebase
* __EditorconfigCheck:__ verifies whether the file adheres to the specified
  configurations defined in the EditorConfig file, ensuring consistent formatting
  across different editors and IDEs used by multiple contributors in a project
* __Markdownfilescheck:__  verifies whether the file adheres to the specified
  configurations defined in the EditorConfig file, ensuring consistent formatting
  across different editors and IDEs used by multiple contributors in a project

### Stage 2: UnitTests

Unit tests are a type of test in software testing that examine individual pieces
(units) of software code to ensure that each part is working correctly.
Unit tests are used to ensure the correctness of small, isolated pieces of
program code.

### Stage 3: Code Style & Security Checks

* __SonarcloudTest:__ evaluates code quality and security analysis. It inspects the
  codebase, identifies potential bugs, security vulnerabilities and provides detailed
  reports and insights to enhance code quality and maintainability
* __SnykTest:__ security analysis that focuses on identifying vulnerabilities within
  project dependencies. It scans the project's dependencies, flags any known security
  issues, and provides guidance on fixing or patching these vulnerabilities to bolster
  overall project security

### Stage 4: Build

The application build artifacts are used to create a Docker image and upload it
to the DockerHub.

### Stage 5: Trivy

It inspects container images and their components to identify potential security
issues, including OS packages, application libraries, and other dependencies.

### Stage 6: Deploy Image To Minikube

Runs minikube and pulls an image from DockerHub and applies the kubernetes
manifests from the project repository.

## Start the project

The program can be launched with Docker and Minikube.

### Requirements for launching from Minikube

* __Installed Docker__
* __Install Minikube__
* __Install kubectl__

#### Step 1: Building the Docker Image

docker build -t image-name .

#### Step 2: Running the Container

docker run -p 5000:5000 image-name

#### Step 3: Start Minikube

minikube start

#### Step 4: Apply the yaml files

Change the container image in the deployment.yaml file to your image

kubectl apply -f deployment.yaml  
kubectl apply -f service.yaml

#### Step 5: Verify that everything is up and running

kubectl get pods
kubectl get deployments
kubectl get services

You should see the name of the image. Against it you must:

At kubectl get pods - in the Status field to write Running

At kubectl get deployments - on the Ready fiels to write 1/1

At kubectl get services - on the External-IP field to write 1/1

#### Step 6: Run the project

minikube service image-name

The project will run in your cluster and open it in your default Web Browser.
