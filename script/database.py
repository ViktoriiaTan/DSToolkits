import psycopg2

def init_db():
    db_params = {
        'host': 'postgres',  # Name of your database service as defined in docker-compose
        'database': 'milestone_3',
        'user': 'admin',
        'password': 'secret'
    }
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mnist_images (
            id SERIAL PRIMARY KEY,
            digit_image BYTEA NOT NULL,
            prediction TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    
def save_to_db(image_data, prediction):
    db_params = {
        'host': 'postgres',
        'database': 'milestone_3',
        'user': 'admin',
        'password': 'secret'
    }
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO mnist_images (digit_image, prediction)
            VALUES (%s, %s)
        """, (psycopg2.Binary(image_data), prediction))
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
