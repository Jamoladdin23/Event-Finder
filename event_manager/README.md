# Event Management API

## Overview

This is a Django REST framework-based API application for managing events. Users can create events, register for them, leave reviews, and receive notifications about changes.

## Features

- User registration and authentication
- CRUD operations for events
- Event registration and ticket booking
- Review and rating system
- Notifications for event updates and registrations

## Requirements

- Python 3.8+
- Docker
- Docker Compose

## Setup and Installation

1. **Clone the repository**:
    ```bash
<<<<<<< HEAD
    git clone <https://github.com/Jamoladdin23/Event-Finder.gitl>
=======
    git clone <https://github.com/Jamoladdin23/Event-Finder.git>
>>>>>>> master
    cd <event_manager>
    ```

2. **Build and run the project using Docker**:
    ```bash
    docker-compose up --build
    ```

3. **Create a superuser**:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. **Access the application**:
    - API Documentation: `http://localhost:8000/swagger/`
    - Admin Panel: `http://localhost:8000/admin/`

## API Endpoints

Refer to the Swagger documentation for a comprehensive list of API endpoints and their usage.

## Running Tests

To run tests, use the following command:
```bash
docker-compose exec web python manage.py test
