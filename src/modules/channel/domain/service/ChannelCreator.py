from src.modules.channel.domain.ChannelRepositoryInterface import ChannelRepositoryInterface
from src.modules.channel.domain.model.Channel import Channel


class ChannelCreator:
    def __init__(self, channel_repository: ChannelRepositoryInterface) -> None:
        self._channel_repository = channel_repository

    def execute(self, channel: Channel) -> None:
        self._channel_repository.add(channel)
