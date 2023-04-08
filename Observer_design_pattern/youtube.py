from user import User
from channel import Channel
from video import Video

class Youtube:
    if __name__ == '__main__':
        vid1 = Video('oberver lecture')
        vid2 = Video('DSA')
        user1 = User('Sourabh')
        user2 = User('Digvijay')
        channel1 = Channel('Design pattern')
        channel1.add_subscriber(user1)
        channel1.add_notify(user1)
        channel1.publish_video(vid1)
        channel1.notify_subscribers(vid1)
        print("subscriber list :", [user.name for user in channel1.subscriber_list ])
        print('notify list : ', [user.name for user in channel1.notify_list])
        channel1.add_subscriber(user2)
        channel1.add_notify(user2)
        channel1.publish_video(vid2)
        channel1.notify_subscribers(vid2)
        print("subscriber list :", [user.name for user in channel1.subscriber_list ])
        print('notify list : ', [user.name for user in channel1.notify_list])
        print('')


