from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from os import environ
import psycopg2


app = FastAPI()

DB_HOST = environ.get("POSTGRES_HOST", "localhost")
DB_NAME = environ.get("POSTGRES_DB", "pingpongdb")
DB_USER = environ.get("POSTGRES_USER", "pingponguser")
DB_PASSWORD = environ.get("POSTGRES_PASSWORD", "password")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )



@app.get("/pingpong", response_class=PlainTextResponse)
def respond_pong():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE counter SET value = value + 1 RETURNING value;")
    new_value = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return f"pong {new_value}"


@app.get("/pings", response_class=PlainTextResponse)
def get_counter():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT value FROM counter LIMIT 1;")
    value = cur.fetchone()[0]

    cur.close()
    conn.close()

    return str(value)