# Event Management System with Django and REST APIs

This is an Event Management System web application developed using Django framework and REST APIs. The system allows users to manage events, register for events, and provides various administrative features for event organizers.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Models](#models)
- [Database](#database)
- [Serializers](#serializers)
- [Views](#views)
- [URLs](#urls)
- [Authentication and Authorization](#authentication-and-authorization)
- [Admin-related APIs](#admin-related-apis)
- [Participant-related APIs](#participant-related-apis)
- [Docker Setup](#docker-setup)

## Overview:

The Event Management System is designed to simplify the process of organizing and participating in events. Users can create and manage events, view upcoming events, register for events, and more. The application is built using Django, a powerful Python web framework, and employs REST APIs for data exchange.

## Requirements:

To run this application, you need:

- Python 3.6 or higher
- Django 3.1 or higher
- Django REST Framework
- JWT for authentication
- Docker (optional, for Docker setup)

## Setup:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a new Django project using `django-admin startproject event_project`.
4. Create a new app within the project using `python manage.py startapp event_app`.
5. Configure the database settings in the `settings.py` file.
6. Run the migrations using `python manage.py makemigrations` and `python manage.py migrate`.
7. Create a superuser using `python manage.py createsuperuser` to access the Django admin panel.

## Models:

The application defines the following models:

- Event: Represents an event with details like title, description, date, time, location, and capacity.
- Attendee: Stores information about users registered for an event.
- Venue: Contains information about event venues.
- User: Extends Django's default user model to add additional fields for roles and authentication.

## Database:

Django's migration system is used to create and update database tables. Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Serializers

Serializers are created using Django REST Framework to convert model instances to JSON and vice versa. These serializers play a crucial role in data serialization and deserialization for API endpoints. Additionally, validation logic is implemented within the serializers to enforce business rules and ensure data integrity.

## Views

Views handle API endpoints and interact with models. Authentication and authorization logic is implemented, differentiating between admin and participant roles. Permissions are enforced for editing or deleting events.

## URLs

URLs for API endpoints are defined in the project's URL configuration file (`urls.py`). They are mapped to their corresponding views. Appropriate permissions are set to restrict access based on user roles.

## Authentication and Authorization

The application uses JSON Web Tokens (JWT) for authentication. Authentication views and logic for issuing and verifying tokens are implemented. Additional logic is included for authorization of admin-only functionality.

## Admin-related APIs

The following APIs are available for event organizers:

- Create, edit, and delete events.
- View and manage user registrations for each event.
- Accept or reject registration requests.
- Manage venue information: add, edit, and remove venues.

## Participant-related APIs

The following APIs are available for event participants:

- View upcoming events.
- Filter events based on categories, tags, date, or location.
- View detailed event information: title, description, date, time, location, and capacity.
- Register for events by providing necessary information.

## Docker Setup

If you prefer to use Docker for environment setup, follow these steps:

1. Install Docker on your system.
2. Use the provided `Dockerfile` and `docker-compose.yml` to build and run the application in a Docker container.


