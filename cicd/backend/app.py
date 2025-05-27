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
    return 'Flask API is running.'

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", ('sainadh',))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)