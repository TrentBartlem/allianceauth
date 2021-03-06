from django.conf import settings
from django.utils import timezone


def is_corp(request):
    return {'IS_CORP': settings.IS_CORP}

def corp_id(request):
    return {'CORP_ID': settings.CORP_ID}

def corp_name(request):
    return {'CORP_NAME': settings.CORP_NAME}

def alliance_id(request):
    return {'ALLIANCE_ID': settings.ALLIANCE_ID}

def alliance_name(request):
    return {'ALLIANCE_NAME': settings.ALLIANCE_NAME}

def jabber_url(request):
    return {'JABBER_URL': settings.JABBER_URL}

def member_api_mask(request):
    return {'MEMBER_API_MASK': settings.MEMBER_API_MASK}

def blue_api_mask(request):
    return {'BLUE_API_MASK': settings.BLUE_API_MASK}

def domain_url(request):
    return {'DOMAIN': settings.DOMAIN, 'MUMBLE_URL': settings.MUMBLE_URL,
            'FORUM_URL': settings.FORUM_URL,
            'ENABLE_AUTH_FORUM': settings.ENABLE_AUTH_FORUM,
            'ENABLE_AUTH_JABBER': settings.ENABLE_AUTH_JABBER,
            'ENABLE_AUTH_MUMBLE': settings.ENABLE_AUTH_MUMBLE,
            'ENABLE_AUTH_IPBOARD': settings.ENABLE_AUTH_IPBOARD,
            'ENABLE_AUTH_TEAMSPEAK3': settings.ENABLE_AUTH_TEAMSPEAK3,
            'ENABLE_AUTH_DISCORD': settings.ENABLE_AUTH_DISCORD,
            'ENABLE_BLUE_JABBER': settings.ENABLE_BLUE_JABBER,
            'ENABLE_BLUE_FORUM': settings.ENABLE_BLUE_FORUM,
            'ENABLE_BLUE_MUMBLE': settings.ENABLE_BLUE_MUMBLE,
            'ENABLE_BLUE_IPBOARD': settings.ENABLE_BLUE_IPBOARD,
            'ENABLE_BLUE_TEAMSPEAK3': settings.ENABLE_BLUE_TEAMSPEAK3,
            'ENABLE_BLUE_DISCORD': settings.ENABLE_BLUE_DISCORD,
            'TEAMSPEAK3_PUBLIC_URL': settings.TEAMSPEAK3_PUBLIC_URL,
            'JACK_KNIFE_URL': settings.JACK_KNIFE_URL,
            'DISCORD_SERVER_ID': settings.DISCORD_SERVER_ID,
            'CURRENT_UTC_TIME': timezone.now()}
