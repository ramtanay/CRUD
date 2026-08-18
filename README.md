
# 🛒 MySQL Product CRUD Manager

<div align="center">

### A modular Python application for performing CRUD operations with MySQL

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MySQL Connector](https://img.shields.io/badge/MySQL%20Connector-Python-F29111?style=for-the-badge&logo=mysql&logoColor=white)

**Create · Read · Update · Delete**

</div>

---

## 📌 Overview

**MySQL Product CRUD Manager** is a Python-based database application that demonstrates how to connect a Python program with a MySQL database and perform the four fundamental **CRUD operations**:

> **C**reate → **R**ead → **U**pdate → **D**elete

The project automatically creates the required database and product table, then demonstrates inserting, retrieving, updating, and deleting product records.

The application is structured into separate Python modules, making the code easier to understand, maintain, and extend.

---

## ✨ Features

- 🔌 **MySQL Database Connection**
  - Connects Python with a local MySQL server.

- 🗄️ **Automatic Database Creation**
  - Creates the `testpy` database if it doesn't already exist.

- 📦 **Automatic Table Creation**
  - Creates the `products` table when required.

- ➕ **Insert Products**
  - Adds new products with ID, name, price, and quantity.

- 🔍 **Fetch Products**
  - Retrieves and displays stored product records.

- ✏️ **Update Products**
  - Updates product information using the product ID.

- 🗑️ **Delete Products**
  - Removes products using their unique ID.

- 🧩 **Modular Architecture**
  - Database operations are separated into dedicated Python modules.

- 💾 **Transaction Handling**
  - Uses `commit()` to save database changes.

---

# 🏗️ Project Structure

All project files are located directly in the repository root:

```text
CRUD/
│
├── config.py
├── create_table.py
├── insert.py
├── fetch.py
├── update.py
├── delete.py
├── executer.py
├── requirements.txt
├── README.md
└── LICENSE
````

### 📄 File Responsibilities

| File               | Responsibility                                    |
| ------------------ | ------------------------------------------------- |
| `config.py`        | MySQL connection and database initialization      |
| `create_table.py`  | Creates the `products` table                      |
| `insert.py`        | Inserts product records                           |
| `fetch.py`         | Retrieves product records                         |
| `update.py`        | Updates product records                           |
| `delete.py`        | Deletes product records                           |
| `executer.py`      | Main execution file demonstrating CRUD operations |
| `requirements.txt` | Python project dependencies                       |
| `README.md`        | Project documentation                             |

---

# 🔄 Application Architecture

```text
                    ┌─────────────────────┐
                    │     executer.py     │
                    │    Main Program     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      config.py      │
                    │ MySQL Configuration │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     MySQL Server    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       testpy        │
                    │      Database       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      products       │
                    │       Table         │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
          INSERT             READ             UPDATE
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                            DELETE
```

---

# 🗃️ Database Schema

The application creates the following database:

```text
Database: testpy
```

Inside the database:

```text
Table: products
```

### `products` Table

| Column     | Data Type     | Constraint    | Description               |
| ---------- | ------------- | ------------- | ------------------------- |
| `id`       | `INT`         | `PRIMARY KEY` | Unique product identifier |
| `name`     | `VARCHAR(25)` | —             | Product name              |
| `price`    | `INT`         | —             | Product price             |
| `quantity` | `INT`         | —             | Available quantity        |

### Example Records

| ID | Product  |  Price | Quantity |
| -: | -------- | -----: | -------: |
|  1 | Phone    | 30,000 |       40 |
|  2 | Pendrive |    900 |       32 |
|  3 | Tab      | 29,000 |       22 |
|  4 | Laptop   | 90,000 |       82 |

---

# 🛠️ Tech Stack

| Technology                | Purpose                      |
| ------------------------- | ---------------------------- |
| 🐍 Python                 | Application logic            |
| 🐬 MySQL                  | Relational database          |
| 🔗 MySQL Connector/Python | Python ↔ MySQL communication |
| 💻 Terminal               | Application execution        |

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/ramtanay/CRUD.git
cd CRUD
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

The project includes a `requirements.txt` file.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 4. Configure MySQL

Make sure your **MySQL Server is installed and running**.

Open:

```text
config.py
```

Configure your MySQL credentials:

```python
user = "root"
password = "YOUR_MYSQL_PASSWORD"
host = "localhost"
port = 3306
```


The application will automatically create the `testpy` database if it does not already exist.

---

# 🚀 Running the Project

Once MySQL is running and the dependencies are installed:

```bash
python executer.py
```

The program will execute the CRUD workflow:

```text
        ┌──────────────────┐
        │ Create Database  │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Create Table     │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Fetch Records    │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Insert Products  │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Fetch Records    │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Update Product   │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Fetch Records    │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Delete Product   │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Fetch Records    │
        └──────────────────┘
```

---

# 💡 CRUD Operations

## 🟢 Create — Insert Data

Products can be inserted using:

```python
insert_data(1, "Phone", 30000, 40)
```

This represents:

```text
ID       → 1
Name     → Phone
Price    → 30000
Quantity → 40
```

Equivalent SQL:

```sql
INSERT INTO products
VALUES (1, 'Phone', 30000, 40);
```

---

## 🔵 Read — Fetch Data

Retrieve all products using:

```python
fetch_data()
```

Equivalent SQL:

```sql
SELECT * FROM products;
```

Example output:

```text
(1, 'Phone', 30000, 40)
(2, 'Pendrive', 900, 32)
(3, 'Tab', 29000, 22)
(4, 'Laptop', 90000, 82)
```

---

## 🟡 Update — Modify Data

The project can update a product using its ID.

Example:

```python
update_data("Price", 2, 1000)
```

Equivalent SQL:

```sql
UPDATE products
SET Price = 1000
WHERE id = 2;
```

---

## 🔴 Delete — Remove Data

A product can be deleted using its ID:

```python
delete_data(3)
```

Equivalent SQL:

```sql
DELETE FROM products
WHERE id = 3;
```

---

# 🧠 Concepts Demonstrated

This project provides hands-on practice with:

### Python

* Functions
* Modules
* Imports
* Function arguments
* Variables
* String formatting
* Database programming

### MySQL

* Databases
* Tables
* Primary keys
* SQL statements
* `CREATE DATABASE`
* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`

### Python + MySQL

* MySQL connections
* Cursors
* `cursor.execute()`
* `fetchall()`
* Transactions
* `connection.commit()`

---

# 🔐 Security Considerations

This project is primarily intended for learning Python-MySQL integration and CRUD operations.

The current implementation uses dynamically constructed SQL statements in some places. For production applications, SQL values should be passed using **parameterized queries** instead of directly constructing SQL with Python strings.

### ❌ Avoid

```python
sql = f"DELETE FROM products WHERE id = {id}"
```

### ✅ Prefer

```python
sql = "DELETE FROM products WHERE id = %s"
cur.execute(sql, (id,))
conn.commit()
```

Parameterized queries help prevent **SQL injection** and are the recommended approach when working with external or user-provided values.

---

# 📦 Dependencies

Project dependencies are maintained in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

The project can be extended into a more complete product management application.

* [ ] 🔐 Replace dynamic SQL with parameterized queries
* [ ] ⚠️ Add exception handling
* [ ] 🧹 Properly close database connections and cursors
* [ ] ✅ Add input validation
* [ ] 🖥️ Build an interactive CLI menu
* [ ] 🔎 Add product search
* [ ] 📊 Add inventory/stock management
* [ ] 📝 Add logging
* [ ] 🔑 Move credentials to environment variables
* [ ] 🧪 Add unit and integration tests
* [ ] 🌐 Build a REST API using Flask or FastAPI
* [ ] 🎨 Add a web-based frontend
* [ ] 📈 Add product analytics and reporting

---

# 🎯 Learning Objective

The primary objective of this project is to understand how a Python application communicates with a relational database and how CRUD operations are implemented programmatically.

The complete data flow can be summarized as:

```text
┌─────────────┐
│   Python    │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ MySQL Connector     │
│      /Python        │
└──────┬──────────────┘
       │
       ▼
┌─────────────┐
│ MySQL Server│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   testpy    │
│   Database  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  products   │
│    Table    │
└─────────────┘
```

---

# 📚 What I Learned

Through this project, I gained practical experience in:

* Connecting Python applications to MySQL
* Creating and managing databases
* Creating relational tables
* Executing SQL commands from Python
* Implementing CRUD operations
* Working with MySQL cursors
* Handling database transactions
* Structuring a Python project into multiple modules

---

# 🚧 Project Status

**Status:** 🟢 Completed — Basic CRUD Implementation

The current version demonstrates the fundamental CRUD workflow using Python and MySQL.

Future versions can evolve this project into a complete **inventory/product management system** with validation, authentication, APIs, testing, and a web interface.

---

# 👨‍💻 Author

## Ramtanay Chakraborty

Engineering graduate interested in:

* 🤖 Artificial Intelligence & Machine Learning
* 🐍 Python Development
* 🗄️ Backend Development
* 📊 Data Analytics
* 🧠 Generative AI

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Python 🐍 × MySQL 🐬 × CRUD ⚡**

Made with ❤️ while learning backend & database development.

</div>

