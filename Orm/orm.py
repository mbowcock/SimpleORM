def mapObjects(rows, columns, myClass):
    recs = []
    for row in rows:
        c = myClass()
        i = 0
        for column in columns:
            setattr(c, column[0], row[i])
            i += 1
        recs.append(c)
    return recs

