import sqlite3


def update_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    ALTER TABLE users
    ADD COLUMN situacao TEXT DEFAULT 'A'
    ''')
    
    cursor.execute('''
    UPDATE users
    SET situacao = 'A'
    WHERE situacao IS NULL
    ''')
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    update_db()
