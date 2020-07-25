import pymysql

conn = pymysql.connections.Connection(host='localhost', user='root', password='tangtang', database='my')
cur = conn.cursor()
for i, j in enumerate(range(10, 1000)):
    sql = cur.execute('insert mytable values({0},{1},{2});'.format(j, j, i))
    conn.rollback()
    conn.commit()
    cur.execute('select func1(1);')
    print(cur.fetchone())

