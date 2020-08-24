from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings

from rocketchat_API.rocketchat import RocketChat


class Command(BaseCommand):
    help = 'Creating channels'

    def handle(self, *args, **kwargs):
        rocket = RocketChat(settings.ROCKET_USERNAME, settings.ROCKET_PASSWORD, server_url=settings.SERVER_URL, proxies=settings.PROXY_DICT)
        channel_names = ["random", "lessons", "python", "django", "react"]
        user_infos = [
            ("example@gmail.com", "Tom Rock", "Aa123456", "tom"), 
            ("example1@gmail.com", "Harry Rock", "Aa123456", "harry"), 
            ("example2@gmail.com", "Angelina Rock", "Aa123456", "angelina"), 
            ("example3@gmail.com", "Jerry Rock", "Aa123456", "jerry"), 
            ]

        for channel in channel_names:
            rocket.channels_create(name = channel)
            rocket.chat_post_message("Hello World!", channel= channel)
        
        for user in user_infos:
            rocket.users_create(email= user[0], name = user[1], password = user[2], username = user[3])

        self.stdout.write(self.style.SUCCESS('5 channels, 5 messages and four users were created with success!'))
        
       