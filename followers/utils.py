from django.contrib.auth.models import User

from followers.models import Relationship


def get_followers(user):
    relationships = Relationship.objects.filter(target=user).select_related('origin')
    followers = list()
    for relationship in relationships:
        followers.append(relationship.origin)
    return followers


def get_following(user):
    pass