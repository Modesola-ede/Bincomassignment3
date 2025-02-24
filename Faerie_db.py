import psycopg2

hostname = 'localhost'
database = 'Faerie'
username = 'postgres'
pwd = 'Beadazzled'
port_id = 5432

def postgres_database():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id,
        )
        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS faerie')

        create_script = """CREATE TABLE IF NOT EXISTS faerie (
                            ID          INT PRIMARY KEY,
                            Name        VARCHAR(40) NOT NULL,
                            Role        VARCHAR(50)
        )"""
        cur.execute(create_script)

        insert_script = "INSERT INTO faerie (ID, Name, Role) VALUES (%s, %s, %s)"
        insert_values = [
            (1, 'Cardan', 'High King Of Elfhame'),
            (2, 'Jude', 'High Queen Of Elfhame'),
            (3, 'Locke', 'Master Of Revels'),
            (4, 'Madoc', 'Commander Of Royal Army'),
        ]

        for record in insert_values:
            cur.execute(insert_script, record)

        cur.execute('SELECT * FROM faerie')
        for record in cur.fetchall():
            print(record)

        update_script = "UPDATE faerie SET Role = 'Ex Commander Of Royal Army' WHERE ID = 4"
        cur.execute(update_script)

        delete_script = 'DELETE FROM faerie WHERE name = %s'
        delete_record = ('Locke',)
        cur.execute(delete_script, delete_record)

        conn.commit()

    except Exception as error:
        print("Error:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()




