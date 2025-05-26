from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host='20.121.42.108',
        database='myappdb',
        user='sainadh',
        password='prudent123'
    )

@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Connected to DB: {db_version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
