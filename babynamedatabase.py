import psycopg2
import re
import os

hostname = 'localhost'
database = 'stress'
username = 'postgres'
pwd = 'Beadazzled'
port_id = 5432
conn = None
cur = None

def finalbabynames():
    file_path = r"C:\Users\Modesola\Downloads\baby2008.html"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as babynames:
            babynames_text = babynames.read()
            filter_text = re.sub(r'<[^>]+>', '', babynames_text)
            names = re.findall(r'\b[A-z][a-z]+\b', filter_text)
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS stress')

        create_script = """ CREATE TABLE IF NOT EXISTS stress (
                            ID          SERIAL PRIMARY KEY,
                            Name        TEXT UNIQUE
                            );
        """
        cur.execute(create_script)

        for name in names:
            try:
             insert_script = "INSERT INTO stress (Name) VALUES (%s) ON CONFLICT (Name) DO NOTHING"
             cur.execute(insert_script, (name,))
            except Exception as error2:
                print(error2)

        cur.execute('SELECT * FROM stress')
        for record in cur.fetchall():
            print(record)

        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()