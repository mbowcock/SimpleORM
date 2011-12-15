import sqlite3
from Orm import orm

class Url:
    id = 0
    longUrl = ''
    shortUrl = ''

cnx = sqlite3.connect('/home/matt/test.db')
cur = cnx.cursor()

rows = cur.execute("select id, longUrl, shortUrl from urls").fetchall()
columns = cur.description

urls = orm.mapObjects(rows, columns, Url)

for u in urls:
    print("ID = {0}\nLong Url = {1}\nShort Url = {2}\n\n".format(u.id, u.longUrl, u.shortUrl))

