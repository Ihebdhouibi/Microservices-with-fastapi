# Microservices with FastAPI

<p align="center"> A simple use case of fastapi microservices project 
<hr width="100px">

<br>
<div align="center">

  ![GitHub Repo stars](https://img.shields.io/github/stars/Ihebdhouibi/Microservices-with-fastapi?style=social)
  ![GitHub language count](https://img.shields.io/github/languages/count/Ihebdhouibi/Microservices-with-fastapi?style=social)
  ![Twitter Follow](https://img.shields.io/twitter/follow/dhouibi_iheb?style=social)
  <br>
  
  [![LinkedIn][linkedin-shield]][linkedin-url]
</div>




</p>

<br>

<details open>
<summary> <strong>Table of content</strong> </summary>

<br>
<ul>
  <li><a href="#about">About the project </a></li>
  <li><a href="#TechStack">Tech Stack</a></li>
  <li><a href="#Installation">Installation</a></li>
  <li><a href="Run">Run project</a></li>
  <li><a href="Demo">Demo</a></li>
  <li><a href="#License">License</a></li>
  <li><a href="#Contact">Contact</a></li>
  
</details>


## <a name="about"></a>About the project 

<p>
Microservice is the approach of breaking down large monolith application into individual applications specializing
in a specific service/functionality. <br>
This approach is often known as <b> Service-Oriented Architecture </b> or <b>SOA</b>.<br>
In a microservice architecture, the application is broken down into several separate services that run in separate processes.
There is a different database for different functionality of the application and the services communicate with each other using the HTTP, AMQP, or a binary protocol like TCP, depending on the nature of each service. 
<br> <br>
This is a simple e-shop app that uses microservices, the aim of this project is to gain hands-on-experience developing 
microservices using python FastAPI, communicate with a JS frontend and deploy docker images to a registry.
</p>


## <a name="TechStack"></a>Tech Stack
***Client :*** React, Bootstrap <br>
***Server :*** Fastapi, Redis <br> 
***CI/CD:*** Docker, Dockerhub

## <a name="Installation">Installation </a>

To run this project follow the instructions below : 
<br>

Clone this repo <br>
```bash
    cd Destination_folder
    git clone https://github.com/Ihebdhouibi/Microservices-with-fastapi.git
```
Run the following command <br>
 

```bash
    cd Microservices-with-fastapi
    pip install -r requirements.txt
``` 
```bash
    cd Microservices-with-fastapi/inventory-frontend
    npm install
```

## <a name="Run">Run project </a>

To run this project execute the following commands 
```bash
    cd Microservices-with-fastapi/inventory
    uvicorn main:app --reload
    python consumer.py
```

```bash
    cd Microservices-with-fastapi/payment
    uvicorn main:app --reload --port=8001
    python consumer.py
```

```bash
    cd Microservices-with-fastapi/inventory-frontend
    npm start
```

## <a name="Demo">Demo </a>
You can also run demo version of this project by downloading the Docker images from DockerHub

## <a name="License">License</a>
Distributed under the MIT License. See LICENSE.txt for more information.

## <a name="Contact">Contact</a>

Email me :email:  <a href="mailto:iheb.dhouibi@polytechnicien.tn"> iheb.dhouibi@polytechnicien.tn </a> <br><br>


[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/Ihebdhouibi/Microservices-with-fastapi/stargazers
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/Ihebdhouibi/Microservices-with-fastapi/network/members
[issues-shield]:https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]:https://github.com/Ihebdhouibi/Microservices-with-fastapi/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dhouibiiheb/