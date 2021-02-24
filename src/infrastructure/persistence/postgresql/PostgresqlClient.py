import psycopg2


class PostgresqlClient(object):
    def __init__(self) -> None:
        host = "localhost"
        port = "5432"
        user = "root"
        password = "root"
        dbname = "youdo"
        dsn = "host=" + host + " port=" + port + " user=" + user + " password=" + password + " dbname=" + dbname
        self._connection = psycopg2.connect(dsn)
        self._connection.autocommit = True
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

