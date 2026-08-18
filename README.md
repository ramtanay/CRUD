# 🛒 MySQL Product CRUD Manager

::: {align="center"}
### A clean Python + MySQL CRUD project for managing product records

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![mysql--connector--python](https://img.shields.io/badge/MySQL%20Connector-Python-F29111?style=for-the-badge)

**Create • Read • Update • Delete**
:::

------------------------------------------------------------------------

## 📌 About the Project

**MySQL Product CRUD Manager** is a beginner-friendly database project
built with **Python** and **MySQL**.

The project demonstrates how a Python application can connect to MySQL
and perform the four fundamental database operations:

-   🟢 **Create** --- Create the database/table and add product records
-   🔵 **Read** --- Retrieve product records
-   🟡 **Update** --- Modify existing product information
-   🔴 **Delete** --- Remove product records

The project is organized into separate Python modules so that each
database operation has its own responsibility.

------------------------------------------------------------------------

## ✨ Features

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  🔌 MySQL Connection                 Connects Python to a local MySQL
                                      server

  🗄️ Database Creation                Automatically creates the `testpy`
                                      database if it does not exist

  📦 Table Creation                   Creates the `products` table
                                      automatically

  ➕ Insert                           Adds new products with ID, name,
                                      price, and quantity

  🔍 Fetch                            Retrieves and displays all product
                                      records

  ✏️ Update                           Updates a selected column for a
                                      product

  🗑️ Delete                           Deletes a product using its ID

  🧩 Modular Structure                CRUD operations are separated into
                                      individual files
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🏗️ Project Structure

``` text
project_db/
│
└── codes/
    ├── config.py          # MySQL connection & database setup
    ├── create_table.py    # Creates the products table
    ├── insert.py          # Inserts product records
    ├── fetch.py           # Retrieves product records
    ├── update.py          # Updates product records
    ├── delete.py          # Deletes product records
    └── executer.py        # Main program / CRUD demonstration
```

### 🔄 Application Flow

``` text
                ┌─────────────────┐
                │   executer.py   │
                └────────┬────────┘
                         │
              ┌──────────▼──────────┐
              │      config.py      │
              │  MySQL Connection   │
              └──────────┬──────────┘
                         │
                    ┌────▼────┐
                    │ testpy  │
                    └────┬────┘
                         │
                  ┌──────▼──────┐
                  │   products  │
                  │    table    │
                  └──────┬──────┘
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
    INSERT             FETCH             UPDATE
       │                                   │
       └─────────────────┬─────────────────┘
                         ▼
                       DELETE
```

------------------------------------------------------------------------

## 🗃️ Database Schema

The application creates a database named:

``` text
testpy
```

Inside it, the following table is created:

### `products`

  Column       Data Type       Constraint      Description
  ------------ --------------- --------------- --------------------
  `id`         `INT`           `PRIMARY KEY`   Unique product ID
  `name`       `VARCHAR(25)`   ---             Product name
  `price`      `INT`           ---             Product price
  `quantity`   `INT`           ---             Available quantity

### Example Data

    ID Product      Price   Quantity
  ---- ---------- ------- ----------
     1 Phone        30000         40
     2 Pendrive       900         32
     3 Tab          29000         22
     4 Laptop       90000         82

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   🐍 **Python**
-   🐬 **MySQL**
-   🔗 **mysql-connector-python**
-   💻 **Command Line / Terminal**

------------------------------------------------------------------------

## ⚙️ Prerequisites

Before running the project, make sure you have:

### 1. Python installed

Check your Python installation:

``` bash
python --version
```

### 2. MySQL Server installed and running

Make sure your local MySQL server is active.

### 3. MySQL Connector for Python

Install the required package:

``` bash
pip install mysql-connector-python
```

------------------------------------------------------------------------

## 🚀 Getting Started

### 1️⃣ Clone the repository

``` bash
git clone <YOUR_REPOSITORY_URL>
cd project_db
```

### 2️⃣ Configure MySQL

Open:

``` text
config.py
```

Update the credentials if required:

``` python
user = "root"
password = "root"
host = "localhost"
port = 3306
```

> ⚠️ Replace the password with your own MySQL password.

### 3️⃣ Run the application

Navigate to the folder containing `executer.py`:

``` bash
cd codes
```

Then run:

``` bash
python executer.py
```

The application will:

``` text
Create Database
      ↓
Create Table
      ↓
Fetch Existing Records
      ↓
Insert Products
      ↓
Fetch Records
      ↓
Update Product
      ↓
Fetch Records
      ↓
Delete Product
      ↓
Fetch Records
```

------------------------------------------------------------------------

## 💡 CRUD Operations Explained

### ➕ INSERT

Products are inserted using:

``` python
insert_data(1, "Phone", 30000, 40)
```

This represents:

``` text
ID       → 1
Name     → Phone
Price    → 30000
Quantity → 40
```

------------------------------------------------------------------------

### 🔍 READ

All records can be retrieved with:

``` python
fetch_data()
```

The records are fetched using:

``` sql
SELECT * FROM products;
```

------------------------------------------------------------------------

### ✏️ UPDATE

The project can update a specific column using the product ID.

Example:

``` python
update_data("Price", 2, 1000)
```

Conceptually:

``` sql
UPDATE products
SET Price = 1000
WHERE id = 2;
```

------------------------------------------------------------------------

### 🗑️ DELETE

A product can be deleted using its ID:

``` python
delete_data(3)
```

Conceptually:

``` sql
DELETE FROM products
WHERE id = 3;
```

------------------------------------------------------------------------

## 🧠 What This Project Demonstrates

This project is useful for learning the fundamentals of:

-   Python functions
-   Python modules and imports
-   MySQL databases
-   Database connections
-   MySQL cursors
-   SQL queries
-   CRUD operations
-   `CREATE DATABASE`
-   `CREATE TABLE`
-   `INSERT`
-   `SELECT`
-   `UPDATE`
-   `DELETE`
-   Transaction handling with `commit()`
-   Basic project modularization

------------------------------------------------------------------------

## 🔐 Important Note About SQL Queries

This project is primarily intended for **learning CRUD and Python-MySQL
integration**.

The current implementation builds some SQL statements using Python
f-strings. For a production application, values should be passed using
**parameterized queries** rather than directly interpolating user input.

For example, the preferred pattern is:

``` python
sql = "INSERT INTO products VALUES (%s, %s, %s, %s)"
values = (id, name, price, quantity)

cur.execute(sql, values)
conn.commit()
```

This makes the application safer and is the next logical improvement for
the project.

------------------------------------------------------------------------

## 🔮 Future Improvements

Possible upgrades include:

-   [ ] Use parameterized SQL queries throughout the project
-   [ ] Add proper exception handling
-   [ ] Close cursors and connections cleanly
-   [ ] Add input validation
-   [ ] Add a menu-driven CLI
-   [ ] Add search functionality
-   [ ] Add product filtering
-   [ ] Add stock management
-   [ ] Add logging
-   [ ] Add configuration through environment variables
-   [ ] Build a REST API using Flask or FastAPI
-   [ ] Add a web-based frontend
-   [ ] Add automated tests

------------------------------------------------------------------------

## 🎯 Learning Goal

The main goal of this project is to understand how **Python communicates
with a relational database** and how the standard CRUD workflow works.

``` text
Python
  │
  ▼
MySQL Connector
  │
  ▼
MySQL Server
  │
  ▼
Database
  │
  ▼
Products Table
```

------------------------------------------------------------------------

## 👨‍💻 Author

**Ramtanay Chakraborty**

Built as a hands-on project for learning **Python + MySQL + Database
CRUD operations**.

------------------------------------------------------------------------

::: {align="center"}
### ⭐ If you found this project useful, consider giving it a star!

**Python 🐍 + MySQL 🐬 = CRUD Power 💪**
:::
