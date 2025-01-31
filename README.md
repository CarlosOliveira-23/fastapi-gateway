# FastAPI Gateway

**FastAPI Gateway** is a production-ready API Gateway built with **FastAPI** that facilitates communication between multiple microservices in a secure and efficient way. It includes features like JWT authentication, rate limiting, caching, and dynamic routing. This project is designed for those who need to manage and scale multiple services with minimal effort.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Proxying Requests](#proxying-requests)
- [Testing](#testing)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

FastAPI Gateway is designed to manage multiple microservices through a single entry point. It offers the following features:
- **JWT Authentication**: Secure your APIs with JSON Web Tokens.
- **Rate Limiting**: Control the flow of requests to prevent overload.
- **Caching**: Speed up responses by caching frequently requested data.
- **Dynamic Proxy Routing**: Route requests to various services dynamically.
- **Docker Support**: Easy setup with Docker for deployment.

## Features

- **JWT Authentication**: Secure API endpoints with token-based authentication.
- **Microservices Proxying**: Route requests dynamically to various services.
- **Rate Limiting**: Set limits to prevent abuse of your API.
- **Caching**: Cache responses to reduce server load and increase speed.
- **FastAPI & Docker**: Utilize FastAPI for building APIs and Docker for deployment.

## Installation

### Prerequisites

To run the project locally or with Docker, you need to have the following software installed:

- **Python 3.8+**: You can download it from the [official Python website](https://www.python.org/).
- **Docker & Docker Compose**: For containerized deployment. Download from the [official Docker website](https://www.docker.com/).

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/CarlosOliveira-23/fastapi-gateway.git
   cd fastapi-gateway

2. Set up a virtual environment:
   ```bash
   python -m venv .venv

3. Activate the virtual environment:
    ```bash
    On Windows:
        .\.venv\Scripts\activate

    On macOS/Linux:
        source .venv/bin/activate

4. Install dependencies:
    ```bash
   pip install -r requirements.txt

5. Run the app:
    ```bash
    uvicorn src.main:app --reload



## Docker Setup
To run the project in Docker, follow these steps:

1. Build the Docker image:
    ```bash
   docker-compose up --build

2. The app will be available at http://localhost:8000.

3. Access the Swagger UI at http://localhost:8000/docs to interact with the API.



## Usage
Authentication
1. Generate a JWT Token: To generate a token, send a POST request to /auth/token with the required credentials (e.g., username and password). Example:
    ```bash
    curl -X 'POST' 'http://localhost:8000/auth/token' -d '{"username": "test", "password": "password"}'
The response will include the access_token.

2. Authenticate Requests: Use the JWT token to authenticate requests. Include it in the Authorization header as follows:
    Authorization: Bearer <access_token>

   

## Proxying Requests
FastAPI Gateway can proxy requests to other services.

1. Route Requests to Microservices: Send a request to the /api/{service}/{path} endpoint to proxy the request to the appropriate service.
    ```bash
    curl -X 'GET' 'http://localhost:8000/api/service1/some/path'



## Testing
You can test the functionality of the Gateway API using the following methods:

Unit Tests: The project includes unit tests to ensure the core functionality is working as expected.

1. Install dependencies with pip install -r requirements.txt.
    ```bash
    pytest
   
2. Postman/Swagger: You can use the Swagger UI at http://localhost:8000/docs to interact with and test the API endpoints directly.



## Configuration
### Environment Variables
To configure the project, you can set the following environment variables:

- **MICROSERVICES**: Define the available microservices and their endpoints in the src/services/microservices.py file.
- **JWT_SECRET_KEY**: Set your secret key for JWT token generation and validation.
- **JWT_ALGORITHM**: Choose the algorithm for JWT encoding/decoding (e.g., "HS256").
- **JWT_EXPIRATION_TIME**: Set the expiration time for the JWT tokens.


## Microservices Configuration
1. The MICROSERVICES dictionary in the src/services/microservices.py file defines the available services:
    ```bash
   MICROSERVICES = {
    "service1": "http://localhost:5001",
    "service2": "http://localhost:5002"
}

You can modify this to add new services or change the endpoint URLs.



## Contributing
Feel free to open an issue or a pull request if you would like to contribute to this project. Please follow the standard Git workflow:

1. Fork the repository.
2. Create a feature branch.
3. Make changes and commit them.
4. Push to your fork and create a pull request.