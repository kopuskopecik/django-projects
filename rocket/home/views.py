from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect

from rocketchat_API.rocketchat import RocketChat


def home(request):   
    rocket = RocketChat(
        settings.ROCKET_USERNAME, 
        settings.ROCKET_PASSWORD, 
        server_url=settings.SERVER_URL, 
        proxies=settings.PROXY_DICT
        )  # Login the system
    
    channels = []  # To record channels' info
    channel_list = rocket.channels_list().json()["channels"]
    for channel in channel_list:
        channels.append((channel["name"], rocket.channels_history(room_id = channel["_id"]).json()["messages"][::-1]))
    

    messages_list = rocket.im_list().json()["ims"]
    messages_list = [i for i in messages_list if i["msgs"] > 0]
    message_contents = []
    for message in messages_list:
        message_contents.append((message["usernames"][1], rocket.im_history(room_id = message["_id"]).json()["messages"][::-1]))

    me = rocket.me().json()  # Information about me like name, username, avatar    
    
    context = {
        "messages_list": messages_list,
        "message_contents": message_contents,
        "channel_list": channel_list,
        "me": me,
        'channels': channels,
    }
    
    message = request.GET.get('message')  # receiving messages in the channels
    channel = request.GET.get("channel")
    if message and channel:
        rocket.chat_post_message(message, channel= channel)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    direct_message = request.GET.get('direct')  # receiving messages in the direct chatting
    username = request.GET.get("username")
    if direct_message and username:
        print("burası çalıştı mı")
        rocket.chat_post_message(direct_message, channel =username)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return render(request, 'home.html', context)
