from pprint import pprint

import requests
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

COGNITO_DOMAIN = settings.ENV('COGNITO_DOMAIN', default='')
COGNITO_APP_CLIENT_ID = settings.ENV('COGNITO_APP_CLIENT_ID', default='')
COGNITO_APP_CLIENT_SECRET = settings.ENV('COGNITO_APP_CLIENT_SECRET', default='')
COGNITO_REDIRECT_URL = (
        (f'https://{settings.HOST_NAME}' if settings.HOST_NAME else 'http://localhost:8000') +
        '/api/control/redirect/'
)


def login_view(request):
    # Redirect the user to the Cognito Hosted UI for authentication

    auth_url = (
        f"https://{COGNITO_DOMAIN}/login?"
        f"response_type=code&client_id={COGNITO_APP_CLIENT_ID}&"
        f"redirect_uri={COGNITO_REDIRECT_URL}"
    )
    return HttpResponseRedirect(auth_url)


def redirect_view(request):
    # Retrieve the authorization code from the callback request
    code = request.GET.get('code')
    if code:
        # Exchange the code for tokens (access token, ID token, refresh token)
        token_url = f"https://{COGNITO_DOMAIN}/oauth2/token"
        data = {
            'grant_type': 'authorization_code',
            'client_id': COGNITO_APP_CLIENT_ID,
            'client_secret': COGNITO_APP_CLIENT_SECRET,
            'code': code,
            'redirect_uri': COGNITO_REDIRECT_URL,
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(token_url, data=data, headers=headers)

        if response.status_code == 200:
            tokens = response.json()
            # Here, you'll typically:
            # 1. Validate the ID token (JWT) to get user information.
            # 2. Create or retrieve a Django user based on the ID token claims.
            # 3. Store the tokens (securely) for later use (e.g., in the session or a database).
            # 4. Call `login(request, user)` to log in the user in Django.

            # (Example - simplified user creation)
            user_response = requests.get(
                f'https://{COGNITO_DOMAIN}/oauth2/userInfo',
                headers=dict(Authorization=f'Bearer {tokens["access_token"]}')
            )
            if user_response.ok:
                user_info = user_response.json()
                user = User.objects.get_or_create(username=user_info['email'], defaults=dict(email=user_info['email']))[0]
                login(request, user)
                return HttpResponseRedirect('/admin/')

        else:
            pprint(response.json())

    return login_view(request)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
