from collections import deque

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.history = deque()
        self.channel_name = list()
        self.subscribed_channels = list()
        self.feed_list = list()

    def update_name(self, name):
        self.name = name

    def add_subscribed_channel(self, channel_name):
        self.subscribed_channels.append(channel_name)

    def remove_subscribed_channel(self, channel_name):
        self.subscribed_channels.remove(channel_name)

    def add_channel(self, channel_name):
        self.channel_name.append(channel_name)
    
    def notification(self, video):
        print(f'{self.name} new video uploaded "{video.name}"')
    
    def __str__(self):
        return self.name

    