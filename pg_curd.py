import pg_handle


songs_table = '''CREATE TABLE songs
    (ID           INTEGER PRIMARY KEY ,
    NAME          CHAR[20],
    SINGER        CHAR[20],
    LINK          TEXT,
    PATH          TEXT);'''
singer_table = '''CREATE TABLE singer
    (ID           INTEGER PRIMARY KEY ,
    NAME          CHAR[20],
    AGE           INTEGER,
    NATION        CHAR[20]);'''


def update():
    pass


def main():
    pg = pg_handle.PgHandler("testdb", "postgres", "6666")
    pg.execute(songs_table)
    pg.execute(singer_table)


if __name__ == "__main__":
    main()
