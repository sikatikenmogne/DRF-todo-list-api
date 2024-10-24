# Todo List API

This project is a part of the [roadmap.sh](https://roadmap.sh/projects/todo-list-api) project.

## Description

This is a Todo List API built with Django and Django REST Framework. It provides endpoints to manage todo items.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/todoListAPI.git
   cd todoListAPI
   ```
2. **Install dependencies using Poetry**:

    ```sh
    pip install poetry
    poetry install
    ```

3. **Run migrations**:

    ```sh
    poetry run python manage.py migrate
    ```

4. **Start the development server**:

    ```sh
    poetry run python manage.py runserver
    ```

## Usage
You can access the API at http://127.0.0.1:8000/. The available endpoints are:

- `GET /todos/` - List all todo items
- `POST /todos/` - Create a new todo item
- `GET /todos/{id}/` - Retrieve a specific todo item
- `PUT /todos/{id}/` - Update a specific todo item
- `DELETE /todos/{id}/` - Delete a specific todo item

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The hooks are configured in the .pre-commit-config.yaml file. To install the hooks, run:

```sh
pre-commit install
```

To run the hooks manually, use:

```sh
pre-commit run --all-files
```