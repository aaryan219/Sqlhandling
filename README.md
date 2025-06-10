# SQLHandler – Cross-Database SQL Executor (SQL Server, Extensible)

This project provides a reusable and extensible `SQLHandler` class using SQLAlchemy to interact with SQL databases, starting with support for **SQL Server** (ODBC). It allows users to execute and read SQL queries with ease, handling connection setup and execution logic internally.

---

## 🚀 Features

- ✅ Connect to SQL Server or any type of databse (Trusted or Username/Password)
- ✅ Execute any SQL statement (CREATE, INSERT, UPDATE, DELETE, etc.)
- ✅ Read SELECT queries with results
- ✅ Extensible for other databases (PostgreSQL, MySQL, etc.)
- ✅ Safe parameterized queries

---


## ⚙️ Prerequisites

- Python 3.6+
- SQL Server running locally (or remote)
- ODBC Driver 17 for SQL Server installed

Install required Python packages:

```bash
pip install sqlalchemy pyodbc


