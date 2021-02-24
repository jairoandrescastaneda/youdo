from src.infrastructure.persistence.postgresql.PostgresqlClient import PostgresqlClient


class PostgresqlBuildEnvironment(object):
    def __init__(self, client: PostgresqlClient):
        self._client = client

    def create_tables(self):
        self._client.execute("CREATE TABLE channels ("
                             "id serial PRIMARY KEY,"
                             "platform_channel_id varchar NOT NULL,"
                             "name varchar NOT NULL,"
                             "description text NULL,"
                             "platform_id varchar NOT NULL,"
                             "country varchar NULL,"
                             "total_video_uploads integer NULL,"
                             "subscribers integer NULL,"
                             "viewers integer NULL,"
                             "thumbnail varchar,"
                             "published_at TIMESTAMP,"
                             "created_at TIMESTAMP,"
                             "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

    def drop_tables(self):
        self._client.execute("DROP TABLE channels;")
