class Channel(object):
    def __init__(self, id: str, platform_channel_id: str, name: str, description: str, platform_id: str, country: str,
                 total_video_uploads: int, subscribers: int, viewers: int, thumbnail: str, published_at: str,
                 created_at, updated_at) -> None:
        self.id = id
        self.platformChannelId = platform_channel_id
        self.name = name
        self.description = description
        self.platformId = platform_id
        self.country = country
        self.totalVideoUploads = total_video_uploads
        self.subscribers = subscribers
        self.viewers = viewers
        self.thumbnail = thumbnail
        self.publishedAt = published_at
        self.createdAt = created_at
        self.updatedAt = updated_at
