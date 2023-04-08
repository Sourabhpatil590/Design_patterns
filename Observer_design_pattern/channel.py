from channel_interface import Channel_Interface

class Channel(Channel_Interface):
    def __init__(self, name) -> None:
        self.channel_name = name
        self.video_list = list()
        self.subscriber_list = list()
        self.notify_list = list()

    def update_name(self, channel_name):
        self.channel_name = channel_name

    def add_subscriber(self, user):
        self.subscriber_list.append(user)

    def remove_subscriber(self, user):
        self.subscriber_list.remove(user)

    def add_notify(self, user):
        self.notify_list.append(user)

    def remove_notify(self, user):
        self.notify_list.remove(user)

    def publish_video(self, video):
        self.video_list.append(video)
        self.publish_subscribers(video)

    def publish_subscribers(self, video):
        for user in self.subscriber_list:
            user.feed_list.append(video)
    
    def notify_subscribers(self, video):
        for user in self.notify_list:
            user.notification(video)