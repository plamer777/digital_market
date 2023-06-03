# The Digital Market
The application provides API with CRUD functionality for suppliers, products and contacts. There are three
kinds of suppliers - Factory, Retail Network and Individual Entrepreneur in the app having certain hierarchy position.
You can create different suppliers and set connections between them, change suppliers and edit its fields.
Only authorised users with 'is_active' parameter will get access to the API.

The app provides functionality as follows:
 - A new user registration by username and password with receiving JWT tokens
 - User login and refresh access token
 - CRUD any kind of supplier
 - CRUD products and contacts for each supplier
 - Change upper-lever supplier for each supplier
 
---

**Technologies used in the project:**
 
 - Django
 - DRF 
 - Gunicorn
 - Simple JWT
 - Pydantic
 - DRF Spectacular
 - Django Filters
 - Docker
 - Docker-compose

---

**How to start the project:**
To start the app just follow the next steps:
 - Clone the repository
 - Install docker and docker-compose packages by the command `sudo apt install docker.io docker-compose`
 - Create .env file using an example provided below
 - Prepare docker-compose.yaml file (you can change ports, volumes, etc. if you want)
 - Start the app by using `sudo docker-compose up -d --build` command
 - The main page with swagger will be available by the url http://localhost/docs/ (if started locally) or 
 http://yourdomain/docs/ (if started on the server)
 - After that application is ready to process requests
 - To get access to the API you should either set IS_ACTIVE parameter in .env file to True, or you can use 
the next option: `sudo docker exec -it <api container id> /bin/bash` and after that enter the command 
`./manage.py createsuperuser`and follow the steps
 - Use your registration details to get access token. After that you can use the API

---
Example of .env file:

    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db (localhost or name of docker container)
    POSTGRES_PORT=5432
    DEBUG=False
    TITLE=Test title
    DESCRIPTION=test description
    VERSION=1.0.0
    TOKEN_LIFETIME=60 (minutes)
    DJANGO_SECRET=very_weak_secret
    IS_ACTIVE=False


The project was created by Alexey Mavrin in 02 June 2023