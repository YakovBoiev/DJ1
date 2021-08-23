from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'google-oauth2':
        return

    api_url = urlunparse(('https', 'people.googleapis.com', '/v1/people/me', None,
                          urlencode(OrderedDict(personFields='genders',
                              key='AIzaSyC9WV5z2bCrEQTxb3i_UrMMXvu28fmHed4')), None))

    resp = requests.get(api_url, headers={'Accept': 'application/json', 'Authorization':  f'Bearer {response["access_token"]}'})
    if resp.status_code != 200:
        return
