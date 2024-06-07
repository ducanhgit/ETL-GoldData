import psycopg2
conn = psycopg2.connect(
    host ='localhost',
    port = '5432',
    database = 'giavang',
    user = 'postgres',
    password ='123'
)
cur = conn.cursor()
cur.execute()