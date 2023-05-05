# Breaking down monoliths 🪨⛏️

## Microservices-based Calculator Application
This is a microservices-based calculator application that allows users to perform various arithmetic operations. The application is built using Flask and Flask-RESTful and consists of multiple services that are orchestrated using Docker Compose. The frontend of the application is built using HTML and JavaScript.
-----------------------------------
## Services
The application consists of the following services:
+ **Addition Service**: This service provides the functionality to add two numbers.
+ **Subtraction Service**: This service provides the functionality to subtract two numbers.
+ **Multiplication Service**: This service provides the functionality to multiply two numbers.
+ **Division Service**: This service provides the functionality to divide two numbers.
+ **GCD Service**: This service provides the functionality to calculate the Greatest Common Divisor of two numbers.
+ **LCM Service**: This service provides the functionality to calculate the Least Common Multiple of two numbers.
+ **Modulus Service**: This service provides the functionality to calculate the remainder of two numbers after division.
+ **Exponent Service**: This service provides the functionality to calculate the result of a power operation.
+ **Greater Than Service**: This service provides the functionality to check if the first value is greater than the second value.
+ **Less Than Service**: This service provides the functionality to check if the first value is less than the second value.
+ **Equal Service**: This service provides the functionality to check if the first value is equal to the second value.
----------------------------------------------------
## Requirements:
- [docker](https://docs.docker.com/engine/) and [docker-compose](https://docs.docker.com/compose/install/). Follow the guides based on your operating system.
- Internet. Pull docker image `python:3.8-alpine` beforehand to avoid connectivity issues.
----------------------------
## Initial directory structure
```
├── README.md
├── docs
│   └── <documentation related images/files>
├── microservices
│   ├── Docker-compose.yaml
│   ├── landing
│   │   ├── app
│   │   │   ├── app.py
│   │   │   ├── requirements.txt
│   │   │   └── templates
│   │   │       └── index.html
│   │   └── Dockerfile
│   │
```
## Intial Monolith architecture diagram
<sub>
<p align="center">
  <img src="docs/microservices-initial.drawio.png" />
</p><h1></h1>
</sub>


## Converted to Microservices-based architecture diagram
<p align="center">
  <img src="docs/microservices-final.drawio.png" />
  

</p>

-------------------------------
### Build & Run
```
# under the microservices directory
# NOTE: For any code changes to be reflected, the build command must be rerun, and then up
docker-compose build
# run without the -d flag incase you want to observe the logs
docker-compose u
```
### To stop the services in detached mode
```
docker-compose down
````
