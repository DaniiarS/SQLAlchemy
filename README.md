# SQLAlchemy Practice

This repository contains my practice scripts and exercises based on the official [SQLAlchemy documentation](https://docs.sqlalchemy.org/). It includes examples using both **SQLAlchemy Core** and the **ORM (Object Relational Mapper)**.

## 🛠️ Environment Setup

To run the examples in this repo:

### 1. Clone the repository

```bash
git clone https://github.com/DaniiarS/sqlalchemy.git
cd sqlalchemy
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows (CMD)
venv\Scripts\activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
sqlalchemy-practice/
│
├── venv/                  # Virtual environment (excluded via .gitignore)
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
├── core/                  # SQLAlchemy Core examples
├── orm/                   # SQLAlchemy ORM examples
└── models/                # Reusable model definitions (if applicable)
```

## 🧠 Topics Covered

* Engine and Connections
* Metadata and Table Definitions
* SQL Expressions (Core)
* ORM Mappings and Sessions
* CRUD Operations
* Relationships and Joins
* Declarative Base Usage
* Alembic (Migrations) *(optional)*

## 📚 Resources

* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
* [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
* [SQLAlchemy Core Tutorial](https://docs.sqlalchemy.org/en/20/core/tutorial.html)

## ✅ License
This repository is for learning and personal use. No license is applied.