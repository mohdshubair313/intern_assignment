
---

# 📌 Django Assignment – User Auth & Paragraph Analyzer

## 📖 Overview

This project is a Django + Django REST Framework (DRF) based assignment that implements:

* **Custom User Registration & Login (JWT Auth)**
* **Creating Tasks models and User can do CRUD operations** 
* **Done with Bonus task of Celery** integration for async tasks (like sending welcome emails and then print that message to the console.. We also can do sending email to particular email id but for that we can use smtp protocol)
* Proper coding standards & documentation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2️⃣ Create virtual environment (using [uv](https://github.com/astral-sh/uv))

```bash
uv venv
```

### 3️⃣ Activate the environment

```bash
# Windows
.venv\Scripts\activate

# Linux / MacOS
source .venv/bin/activate
```

### 4️⃣ Install dependencies

**All dependency are in pyproject.toml file**

```bash
uv pip install -r requirements.txt
```

### 5️⃣ Setup environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=Default SQLlite database
REDIS_URL=redis://localhost:6379/0
```

### 6️⃣ Run migrations

```bash
uv run python manage.py migrate
```

### 7️⃣ Create a superuser

```bash
uv run python manage.py createsuperuser
```

### 8️⃣ Start services

* Run Django server:

```bash
uv run python manage.py runserver
```

* Start Celery worker:

```bash
uv run celery -A core worker -l info
```

---

## 🔗 API Usage Guide

### Base URL

```
http://127.0.0.1:8000/api/
```

### 1️⃣ Authentication

#### Register User

**POST** `/users/register/`
Request:

```json
{
  "email": "test@example.com",
  "password": "securepassword",
  "name": "Hello"
}
```

Response:

```json
{
  "id": 1,
  "email": "test@example.com",
  "message": "User registered successfully"
}
```

#### Login (JWT)

**POST** `/users/login/`
Request:

```json
{
  "email": "test@example.com",
  "password": "securepassword"
}
```

Response:

```json
{
  "access": "your-jwt-access-token",
  "refresh": "your-jwt-refresh-token"
}
```

---

## 🌟 Bonus Tasks Completed

* ✅ **Custom User Model** with email as username field
* ✅ **JWT Authentication** using `djangorestframework-simplejwt`
* ✅ **Celery Integration** for sending welcome email on user registration
* ✅ **Clean API documentation** included in README
