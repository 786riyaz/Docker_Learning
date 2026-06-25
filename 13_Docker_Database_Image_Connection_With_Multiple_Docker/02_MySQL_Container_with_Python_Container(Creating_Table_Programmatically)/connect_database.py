# pip install mysql-connector-python

import os
import sys
import mysql.connector
from mysql.connector import Error

# connection config (use env vars or defaults)
# MYSQL_HOST = os.environ.get("MYSQL_HOST", "host.docker.internal")
# MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")  # uncomment for non-Docker setup
MYSQL_HOST = os.environ.get("MYSQL_HOST", "172.17.0.2")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "root")
MYSQL_DB = os.environ.get("MYSQL_DB", "amazon")  # DB shown in your phpMyAdmin URL

def ensure_database_exists(host: str, port: int, user: str, password: str, database: str):
    """
    Connect without a default database and create the database if it doesn't exist.
    """
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            connection_timeout=5,
        )
        cursor = conn.cursor()
        db_quoted = f"`{database.replace('`','')}`"
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_quoted};")
        conn.commit()
        print(f"✅ Ensured database exists: {database}")
    except Exception as e:
        print("❌ Error ensuring database exists:", e, file=sys.stderr)
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def connect_mysql(host: str, port: int, user: str, password: str, database: str):
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            connection_timeout=5,
        )
        if conn.is_connected():
            print(f"✅ Connected to MySQL DB '{database}' on {host}:{port}")
            return conn
        raise Error("Connection not established")
    except Exception as e:
        print("❌ MySQL connection error:", e, file=sys.stderr)
        raise

def create_product_table(conn, database: str = MYSQL_DB, table: str = "product"):
    """
    Create a 'product' table if it doesn't exist in the specified database.
    """
    cursor = None
    try:
        cursor = conn.cursor()
        db_quoted = f"`{database.replace('`','')}`"
        table_quoted = f"`{table.replace('`','')}`"
        sql = f"""
        CREATE TABLE IF NOT EXISTS {db_quoted}.{table_quoted} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        cursor.execute(sql)
        conn.commit()
        print(f"✅ Table ensured: {database}.{table}")
    except Exception as e:
        print("❌ Error creating table:", e, file=sys.stderr)
        raise
    finally:
        if cursor:
            cursor.close()

def insert_sample_product(conn, database: str = MYSQL_DB, table: str = "product", name="Sample Product", price=9.99, description="Sample description"):
    cursor = None
    try:
        cursor = conn.cursor()
        db_quoted = f"`{database.replace('`','')}`"
        table_quoted = f"`{table.replace('`','')}`"
        sql = f"INSERT INTO {db_quoted}.{table_quoted} (name, price, description) VALUES (%s, %s, %s);"
        cursor.execute(sql, (name, price, description))
        conn.commit()
        print("✅ Inserted sample product, id:", cursor.lastrowid)
        return cursor.lastrowid
    except Exception as e:
        print("❌ Error inserting sample product:", e, file=sys.stderr)
        raise
    finally:
        if cursor:
            cursor.close()

def fetch_products(conn, database: str = MYSQL_DB, table: str = "product"):
    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        # Quote identifiers to allow hyphens in database/table names and avoid injection
        db_quoted = f"`{database.replace('`','')}`"
        table_quoted = f"`{table.replace('`','')}`"
        sql = f"SELECT * FROM {db_quoted}.{table_quoted};"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("📄 Products from DB:")
        for r in rows:
            print(r)
        return rows
    except Exception as e:
        print("❌ Error fetching products:", e, file=sys.stderr)
        raise
    finally:
        if cursor:
            cursor.close()
        # Do not close conn here; caller manages connection lifecycle.

if __name__ == "__main__":
    # Ensure database exists before connecting with a default database
    ensure_database_exists(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)

    conn = None
    try:
        conn = connect_mysql(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)

        # Create product table (singular) and insert a sample record, then print records
        create_product_table(conn, MYSQL_DB, "product")
        insert_sample_product(conn, MYSQL_DB, "product", name="Example Item", price=19.95, description="An example product inserted by script.")
        fetch_products(conn, MYSQL_DB, "product")

    finally:
        if conn:
            conn.close()
            print("🔌 Connection closed")