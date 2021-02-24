from src.infrastructure.persistence.postgresql.PostgresqlBuildEnvironment import PostgresqlBuildEnvironment
from src.infrastructure.persistence.postgresql.PostgresqlClient import PostgresqlClient

if __name__ == '__main__':
    a = PostgresqlBuildEnvironment(PostgresqlClient())
    a.drop_tables()
    a.create_tables()
