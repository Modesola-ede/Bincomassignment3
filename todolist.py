import psycopg2

hostname = 'localhost'
database = 'todolist'
username = 'postgres'
pwd = 'Beadazzled'
port_id = 5432


def todo():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS todolist')

        create_script = """ CREATE TABLE IF NOT EXISTS todolist (
                            ID          SERIAL PRIMARY KEY,
                            Task        TEXT UNIQUE,
                            STATUS      Boolean
                            );
        """
        cur.execute(create_script)

        insert_script = "INSERT INTO todolist (ID, Task, STATUS) VALUES (%s, %s, %s)"
        insert_values = [
            (1, 'Clean Roon', 'False'),
            (2, 'Wash Clothes', 'True'),
            (3, 'Finish assignments', 'False'),
            (4, 'Check and send mails', 'False'),
            (5, 'Build Website', 'False'),
        ]

        for record in insert_values:
            cur.execute(insert_script, record)

        update_script = "UPDATE todolist SET STATUS = 'True' WHERE ID = 3"
        cur.execute(update_script)

        cur.execute('SELECT * FROM todolist')
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

todo()