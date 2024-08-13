# Database Manager API

This project is a [FastAPI](https://fastapi.tiangolo.com)-based API designed to manage
a [PostgreSQL](https://www.postgresql.org) database using [SQLAlchemy](https://www.sqlalchemy.org).

It provides endpoints for interacting with configuration resources in the database.

## Features

- **Secure Authentication**: Uses `api_key` for security and authentication.
- **CRUD Operations**: Includes functionality to read, add, and remove configuration resources.

## API Endpoints

### `/get_configs/`

- **Method:** GET
- **Description:** Retrieves all configuration resources from the database.

### `/add_new_config/`

- **Method:** POST
- **Description:** Adds a new configuration resource to the database.
- **Request Body:** JSON object with configuration details.

### `/rm_config/{resource_id}`

- **Method:** DELETE
- **Description:** Removes a configuration resource from the database by its `resource_id`.

## Security

The API uses an `api_key` for authentication. Include the `api_key` in the `Authorization` header for all requests.

## Libraries Used

The project employs the following libraries:

- **[FastAPI](https://fastapi.tiangolo.com)**: A modern framework for building APIs with Python.
- **[SQLAlchemy](https://www.sqlalchemy.org)**: A toolkit and ORM for database operations.
- **[psycopg2](https://www.psycopg.org/)**: PostgreSQL adapter for Python.
- **[environs](https://pypi.org/project/environs/)**: Simplifies handling of environment variables.

## Logging

Logs are stored in `src/logs/api.log`. The logging configuration can be adjusted in `src/logger.py`.

## Project Structure

```bash
DatabaseManagerAPI
├── README.md
├── api.json
├── requirements.txt
├── run.py
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── logger.py
│   ├── logs
│   │   ├── api.log
│   │   └── api.log.2024-07-30
│   ├── main.py
│   ├── models.py
│   ├── resources.py
│   └── schemas.py
├── static
│   ├── index.html
│   ├── scripts.js
│   └── styles.css
└── tests
    ├── __init__.py
    ├── test_crud.py
    └── test_routes.py

```

<img width="839" alt="Screenshot 2024-08-13 at 13 14 54" src="https://github.com/user-attachments/assets/f9daf566-d96e-4eed-9216-bd29888a9ee6">
