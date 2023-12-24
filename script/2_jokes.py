import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="student",
    password="123456",
    dbname="postgres"  # Connect to the default database to create a new one
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a new database
with conn.cursor() as cur:
    cur.execute("CREATE DATABASE ms3_jokes;")

conn.close()

# Connect to the new database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="student",
    password="123456",
    dbname="ms3_jokes"
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a table
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE jokes (
            ID SERIAL PRIMARY KEY,
            JOKE TEXT NOT NULL
        );
    """)

# Insert a joke
with conn.cursor() as cur:
    cur.execute("INSERT INTO jokes (JOKE) VALUES (%s) RETURNING ID", ("Q. What is the biggest lie in the entire universe? A. I have read and agree to the Terms & Conditions.",))
    joke_id = cur.fetchone()[0]

# Fetch and print the joke
with conn.cursor() as cur:
    cur.execute("SELECT JOKE FROM jokes WHERE ID = %s", (joke_id,))
    joke = cur.fetchone()[0]
    print(joke)

conn.close()
