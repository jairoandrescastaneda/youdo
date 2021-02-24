from src.infrastructure.persistence.postgresql.PostgresqlClient import PostgresqlClient
from src.modules.channel.domain.ChannelRepositoryInterface import ChannelRepositoryInterface
from src.modules.channel.domain.model.Channel import Channel


class PostgresqlChannelRepository(ChannelRepositoryInterface):
    def __init__(self, client: PostgresqlClient):
        self._client = client

    def add(self, channel: Channel) -> None:
        self._client.execute("INSERT INTO channels ()")