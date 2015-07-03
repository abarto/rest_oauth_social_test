from __future__ import absolute_import, unicode_literals

from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token

from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta
 
 
def get_token_json(access_token):
    return JsonResponse({
        'access_token': access_token.token,
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'refresh_token': access_token.refresh_token.token,
        'scope': access_token.scope
    });
 
 
def get_access_token(user):
    application = Application.objects.get(name="my-api")

    try:
        old_access_token = AccessToken.objects.get(user=user, application=application)
        old_refresh_token = RefreshToken.objects.get(user=user, access_token=old_access_token)
    except:
        pass
    else:
        old_access_token.delete()
        old_refresh_token.delete()
 
    token = generate_token()
    refresh_token = generate_token()
 
    expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    scope = "read write"

    access_token = AccessToken.objects.\
        create(user=user,
               application=application,
               expires=expires,
               token=token,
               scope=scope)
 
    RefreshToken.objects.\
        create(user=user,
               application=application,
               token=refresh_token,
               access_token=access_token)
 
    return get_token_json(access_token)