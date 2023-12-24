import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def init_db():
    # Database connection parameters
    db_params = {
        'host': 'postgres',  # Assuming the PostgreSQL service name is 'postgres' as per your Docker Compose
        'user': 'admin',
        'password': 'secret',
    }

    # Connect to the default PostgreSQL database (template1) to create a new database
    conn = psycopg2.connect(**db_params, dbname='template1')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Create a new database if it doesn't exist
    new_database_name = 'milestone_3'
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s;"), [new_database_name])
    if not cursor.fetchone():
        cursor.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(new_database_name)))

    # Close the connection to template1 and connect to the new database
    conn.close()
    conn = psycopg2.connect(**db_params, dbname=new_database_name)
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS input_data (
            id SERIAL PRIMARY KEY,
            image_data BYTEA
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            input_data_id INTEGER REFERENCES input_data(id),
            prediction_result TEXT
        );
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
