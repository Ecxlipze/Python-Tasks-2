# Task Manager API

A RESTful Task Management API built with Django REST Framework.

## Features

- JWT Authentication
- Role-Based Access Control (Admin / Employee)
- Multi-Tenant Companies
- Project Management
- Task Management
- Soft Delete
- Audit Logging
- API Throttling
- Background Tasks with Celery & Redis

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- Celery
- Redis
- SQLite

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd task-manager
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Start Django

```bash
python manage.py runserver
```

### Start Celery

```bash
celery -A config worker --loglevel=info
```

---

## Authentication

Obtain JWT Token

```
POST /api/token/
```

Refresh Token

```
POST /api/token/refresh/
```

---

## API Endpoints

### Authentication

- POST /api/signup/
- POST /api/token/
- POST /api/token/refresh/

### Projects

- GET /api/projects/
- POST /api/projects/
- GET /api/projects/{id}/
- PUT /api/projects/{id}/
- PATCH /api/projects/{id}/
- DELETE /api/projects/{id}/

### Tasks

- GET /api/tasks/
- POST /api/tasks/
- GET /api/tasks/{id}/
- PUT /api/tasks/{id}/
- PATCH /api/tasks/{id}/
- PATCH /api/tasks/{id}/complete/
- DELETE /api/tasks/{id}/

### Users

- GET /api/users/
- POST /api/users/
- GET /api/users/{id}/
- PUT /api/users/{id}/
- PATCH /api/users/{id}/
- DELETE /api/users/{id}/

---

## Project Structure

```
task-manager/
│
├── accounts/
├── audit/
├── config/
├── core/
├── projects/
├── tasks/
├── docs/
├── manage.py
└── README.md
```

---
