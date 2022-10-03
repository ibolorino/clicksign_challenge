# Clicksign Challenge

## Basic Commands

### Install Docker and Docker Compose

-   Read the docs to install and configure **Docker** and **Docker Compose**:
    https://docs.docker.com/

### Starting up

-   Rename `.env.local` file to `.env`

-   On project folder use this command to build the docker containers:

        $ docker-compose build

-   Run the initial migrate to database:

        $ docker-compose run --rm web python manage.py migrate

-   Up the containers to access a local application on http://localhost:8000/:

        $ docker-compose up

### Setting Up Your Users

-   To create a **superuser account**, use this command:

        $ docker-compose run --rm web python manage.py createsuperuser
