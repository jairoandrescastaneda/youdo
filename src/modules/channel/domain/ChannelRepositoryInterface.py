from src.modules.channel.domain.model.Channel import Channel


class ChannelRepositoryInterface:
    def add(self, channel: Channel) -> None:
        pass
