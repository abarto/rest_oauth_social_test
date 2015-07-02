from __future__ import absolute_import, unicode_literals

from django.conf import settings

from social.backends.oauth import BaseOAuth2


class FakeSocialSiteOAuth2(BaseOAuth2):
    name = 'fake_social_site'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id')
    ]

    def access_token_url(self):
        return settings.FAKE_SOCIAL_SITE_AUTH_AUTHORIZATION_URL

    def authorization_url(self):
        return settings.FAKE_SOCIAL_SITE_AUTH_ACCESS_TOKEN_URL

    def get_user_details(self, response):
        return {
            'username': response.get('username'),
            'email': response.get('email') or '',
            'first_name': response.get('first_name'),
            'last_name': response.get('last_name'),
        }

    def user_data(self, access_token, *args, **kwargs):
        try:
            return self.get_json(
                settings.FAKE_SOCIAL_SITE_AUTH_USER_DETAILS_URL,
                headers={'Authorization': 'Bearer {}'.format(access_token)}
            )
        except ValueError:
            return None


class FakeSocialSiteWithParamOAuth2(BaseOAuth2):
    name = 'fake_social_site_with_param'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id')
    ]

    def access_token_url(self):
        return settings.FAKE_SOCIAL_SITE_WITH_PARAM_AUTH_AUTHORIZATION_URL

    def authorization_url(self):
        return settings.FAKE_SOCIAL_SITE_WITH_PARAM_AUTH_ACCESS_TOKEN_URL

    def get_user_details(self, response):
        return {
            'username': response.get('username'),
            'email': response.get('email') or '',
            'first_name': response.get('first_name'),
            'last_name': response.get('last_name'),
        }

    def user_data(self, access_token, *args, **kwargs):
        try:
            return self.get_json(
                settings.FAKE_SOCIAL_SITE_WITH_PARAM_AUTH_USER_DETAILS_URL.format(**kwargs),
                headers={'Authorization': 'Bearer {}'.format(access_token)}
            )
        except ValueError:
            return None