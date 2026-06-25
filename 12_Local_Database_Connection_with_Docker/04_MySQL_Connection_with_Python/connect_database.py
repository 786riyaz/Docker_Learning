# pip install mysql-connector-python

import os
import sys
import mysql.connector
from mysql.connector import Error

# connection config (use env vars or defaults)
MYSQL_HOST = os.environ.get("MYSQL_HOST", "host.docker.internal")
# MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")  # uncomment for non-Docker setup
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
MYSQL_DB = os.environ.get("MYSQL_DB", "e-commerce")  # DB shown in your phpMyAdmin URL

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

def fetch_products(conn, database: str = MYSQL_DB, table: str = "products"):
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
    except Exception as e:
        print("❌ Error fetching products:", e, file=sys.stderr)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    conn = connect_mysql(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
    fetch_products(conn)