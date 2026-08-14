# FastAPI CRUD API with SQL Server 2022

A RESTful CRUD (Create, Read, Update, Delete) API developed using **FastAPI**, **Python**, **SQL Server 2022**, **SQLAlchemy**, and **Pydantic**.

This project demonstrates how to build a backend REST API for performing CRUD operations with a Microsoft SQL Server 2022 database.

---

## 🚀 Features

* Create a new record
* Retrieve all records
* Retrieve a record by ID
* Update an existing record
* Delete a record
* SQL Server 2022 database connectivity
* SQLAlchemy ORM
* Pydantic data validation
* RESTful API architecture
* Automatic API documentation with Swagger UI
* Automatic API documentation with ReDoc
* Python virtual environment
* Dependency management using `requirements.txt`

---

## 🛠️ Technologies Used

| Technology      | Purpose                         |
| --------------- | ------------------------------- |
| Python          | Programming Language            |
| FastAPI         | Backend Web Framework           |
| SQL Server 2022 | Database                        |
| SQLAlchemy      | Object Relational Mapping (ORM) |
| Pydantic        | Data Validation                 |
| Uvicorn         | ASGI Server                     |
| Git             | Version Control                 |
| GitHub          | Code Repository                 |

---

## 📁 Project Structure

```text
FastAPI_CURD_SQLSERVER/
│
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── database.sql
├── requirements.txt
├── .gitignore
└── README.md
```

> The `venv/` folder is used locally for the Python virtual environment and is excluded from Git using `.gitignore`.

---

## 📌 Project Files

### `app/main.py`

This is the main FastAPI application file.

It contains:

* FastAPI application initialization
* API routes
* HTTP request handling
* CRUD route integration

### `app/database.py`

This file handles the connection between the FastAPI application and SQL Server 2022 using SQLAlchemy.

### `app/models.py`

This file contains the SQLAlchemy database models.

The models represent the database tables used by the application.

### `app/schemas.py`

This file contains Pydantic schemas used for:

* Request validation
* Response validation
* Data serialization

### `app/crud.py`

This file contains the CRUD operations:

* Create
* Read
* Update
* Delete

### `database.sql`

This SQL script contains the database and table-related SQL commands required for the project.

### `requirements.txt`

This file contains the Python packages required to run the application.

### `.gitignore`

This file specifies files and folders that should not be uploaded to GitHub.

For example:

```text
venv/
__pycache__/
*.pyc
.env
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/SayaliPawar1125/FastAPI_CURD_SQLServer.git
```

Move into the project directory:

```bash
cd FastAPI_CURD_SQLSERVER
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```cmd
venv\Scripts\activate
```

After activation, the terminal will display:

```text
(venv)
```

---

## 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🗄️ SQL Server 2022 Setup

This project uses **Microsoft SQL Server 2022** as the database.

Make sure the following are installed and running:

* SQL Server 2022
* SQL Server Management Studio (SSMS)
* Appropriate SQL Server ODBC driver

---

## Create the Database

Open **SQL Server Management Studio (SSMS)** and connect to your SQL Server 2022 instance.

Open the project's:

```text
database.sql
```

file.

Execute the SQL commands to create the required database and tables.

---

# 🔌 Database Configuration

The SQL Server database connection is configured in:

```text
app/database.py
```

A typical SQLAlchemy connection string for SQL Server looks like:

```python
DATABASE_URL = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"
```

Update the connection details according to your SQL Server 2022 configuration.

The connection may contain:

* SQL Server instance name
* Database name
* Username
* Password
* ODBC driver

> **Important:** Do not upload real database passwords or sensitive credentials to GitHub.

---

# ▶️ Run the FastAPI Application

From the project root directory, run:

```bash
uvicorn app.main:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* View API endpoints
* Test API endpoints
* Send GET requests
* Send POST requests
* Send PUT requests
* Send DELETE requests
* View request and response data

---

## ReDoc

FastAPI also provides ReDoc documentation.

Open:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔄 CRUD Operations

CRUD stands for:

| Operation | HTTP Method | Description                |
| --------- | ----------- | -------------------------- |
| Create    | POST        | Creates a new record       |
| Read      | GET         | Retrieves records          |
| Update    | PUT         | Updates an existing record |
| Delete    | DELETE      | Deletes a record           |

The exact API endpoint paths are defined in:

```text
app/main.py
```

---

# 🔁 Application Flow

```text
Client
   │
   ▼
FastAPI Application
   │
   ▼
API Routes
   │
   ▼
CRUD Functions
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQL Server 2022
```

---

# 🧪 API Testing

The API can be tested using:

* Swagger UI
* Postman
* Browser for GET requests
* Other REST API clients

### Using Swagger UI

Start the application:

```bash
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Select an API endpoint and click:

```text
Try it out
```

Enter the required data and click:

```text
Execute
```

The API response will be displayed directly in Swagger UI.

---

# 📦 Python Dependencies

The project dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🔐 Security Considerations

For a production application:

* Do not hard-code database passwords.
* Use environment variables for sensitive information.
* Keep `.env` files out of GitHub.
* Validate incoming API data.
* Use authentication and authorization where required.
* Use HTTPS in production.
* Keep dependencies updated.

---

# 🎯 Learning Objectives

This project was developed to understand and practice:

* Python
* FastAPI
* REST API development
* CRUD operations
* HTTP methods
* SQL Server 2022
* SQLAlchemy ORM
* Pydantic
* Database connectivity
* API routing
* Request and response handling
* Data validation
* Swagger UI
* ReDoc
* Virtual environments
* Python package management
* Git and GitHub

---

# 💡 What I Learned

Through this project, I learned how to:

1. Create a FastAPI application.
2. Configure a SQL Server 2022 database.
3. Connect FastAPI with SQL Server using SQLAlchemy.
4. Create database models.
5. Create Pydantic schemas.
6. Implement CRUD operations.
7. Create REST API endpoints.
8. Validate request data.
9. Test APIs using Swagger UI.
10. Manage Python dependencies using `requirements.txt`.
11. Use Git for version control.
12. Push a FastAPI project to GitHub.

---

# 👩‍💻 Author

## Sayali Pawar

GitHub:

https://github.com/SayaliPawar1125

---

# 📌 Repository

GitHub Repository:

https://github.com/SayaliPawar1125/FastAPI_CURD_SQLServer


