# [Docker Compose with Spring Boot, MySQL, MongoDB, Angular 8, NGINX and Python Flask](https://github.com/nickruta/data_science_pipeline)

## What you'll build
- A collection of Docker Containers connected using Docker Compose. This includes a Spring Boot back end REST Web Service, an Angular 8 Front End (served using NGINX), a Python Flask Machine Learning Microservice and databases using MySQL and MongoDB.

## What you'll need
- Docker CE

## Stack
- Docker
- Java
- Spring Boot
- MySQL
- MongoDB
- Angular 8
- Python Flask
- NGINX
- Maven

## Run
- Run command 'docker-compose build'
- Run command 'docker-compose up'
- Create an admin account using curl command to the springapp service: 'curl -d '{"name":"admin", "username":"admin","email":"admin@admin.com", "role":["admin"], "password":"123456789"}' -H "Content-Type: application/json" -X POST http://localhost:8080/api/auth/signup'
- Access to http://localhost:4200/
- Sign in and view the "Admin Board" to see the detailed dashboard
